import pandas as pd

def ler_arquivo():
    with open('raw_response.json', 'r') as arquivo:
        dados = arquivo.read()

    dados_dict = eval(dados)

    return [linha['_source'] for linha in dados_dict['hits']['hits']]

def normalizar_nomes(valor):
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
    dataframe = dataframe[dataframe['paciente_endereco_nmMunicipio'] != '']
    dataframe['fabricante_nome'] = dataframe['vacina_fabricante_nome'].apply(normalizar_nomes)
    
    return dataframe

def obter_metricas(dataframe):
    agrupado_por_fabricante = dataframe.groupby(by=['fabricante_nome']).size().sort_values(ascending=False).to_dict()
    agrupado_por_fabricante_municipio = dataframe.groupby(by=['fabricante_nome', 'paciente_endereco_nmMunicipio', 'paciente_endereco_uf']).size().sort_values(ascending=False).to_dict()
    resultado_total = dataframe.shape[0]

    return resultado_total, agrupado_por_fabricante, agrupado_por_fabricante_municipio
