import pandas as pd
import json

def ler_arquivo():
    with open('raw_response.json', 'r') as arquivo:
        dados = arquivo.read()

    dados_dict = eval(dados)

    dados_retorno = []

    for linha in dados_dict['hits']['hits']:
        dados_retorno.append(linha['_source'])

    return dados_retorno

def normalizar_nomes(valor):
    # agrupa fabricantes idependente do instituto
    # e da categoria (pediatrica)

    valor_maiusculo = valor.upper()

    if 'ASTRAZENECA' in valor_maiusculo:
        return 'ASTRAZENECA'
    if 'PFIZER' in valor_maiusculo:
        return 'PFIZER'
    if 'SINOVAC' in valor_maiusculo:
        return 'SINOVAC'

    return valor_maiusculo

def criar_dataframe(dados):
    dataframe = pd.DataFrame(dados)

    # ignora municipios com nome vazio
    dataframe = dataframe[dataframe['paciente_endereco_nmMunicipio'] != '']
    dataframe['fabricante_nome'] = dataframe['vacina_fabricante_nome'].apply(normalizar_nomes)
    
    return dataframe

def obter_metricas(dataframe):
    # pergunta 1
    resultado_total = dataframe.shape[0] # quantidade de linhas do dataframe = 995

    # pergunta 2
    agrupado_por_fabricante = dataframe.groupby(by=['fabricante_nome']).size().sort_values(ascending=False).to_dict()

    # pergunta 3
    agrupado_por_fabricante_municipio = dataframe.groupby(by=['fabricante_nome', 'paciente_endereco_nmMunicipio', 'paciente_endereco_uf']).size().sort_values(ascending=False).to_dict()

    return resultado_total, agrupado_por_fabricante, agrupado_por_fabricante_municipio

def preparar_saida(resultado_total, agrupado_por_fabricante, agrupado_por_fabricante_municipio):
    fabricante_por_municipio = {}

    for fabricante, total in agrupado_por_fabricante.items():
        fabricante_por_municipio[fabricante] = {'total_doses': total, 'total_por_municipio': []}

    for (fabricante, cidade, estado), total in agrupado_por_fabricante_municipio.items():
        linha = {"municipio": cidade, "uf": estado, 'total': total}
        fabricante_por_municipio[fabricante]['total_por_municipio'].append(linha)


    fabricante_por_municipio.update({'total_doses_aplicadas': resultado_total})

    return fabricante_por_municipio

def escrever_arquivo_final(formato_final):
    with open('resultado_final.json', 'w') as arquivo:
        arquivo.write(json.dumps(formato_final))

def main():
    dados = ler_arquivo()
    dataframe = criar_dataframe(dados)
    resultado_total, agrupado_por_fabricante, agrupado_por_fabricante_municipio = obter_metricas(dataframe)
    formato_final = preparar_saida(resultado_total, agrupado_por_fabricante, agrupado_por_fabricante_municipio)
    escrever_arquivo_final(formato_final)

if __name__ == '__main__':
    main()
