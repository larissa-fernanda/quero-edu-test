# Teste técnico - Quero Educação

Para a resolução do parte 1, foi utilizado `Python 3.8` e a biblioteca `Pandas`.

O arquivo fornecido `raw_response.json` não está no formato `json` e sim em um dict Python. Foi preciso utilizar a função `eval()` para interpretar o arquivo.

## Instrução para instalação

`pip install -r requirements`

## Saídas da parte 2
- Questão 1
```+-------------------------------------+---------+
|name                                 |somatoria|
+-------------------------------------+---------+
|Ciência de Dados                     |99.9     |
|Engenharia da Computação             |250.0    |
|Ciência da Computação                |359.7    |
|Análise e Desenvolvimento de Sistemas|0.0      |
+-------------------------------------+---------+
```
- Questão 2
```+---+---------------+---------+-----------+
|id |cliente_name   |course_id|mensalidade|
+---+---------------+---------+-----------+
|23 |João da Silva  |10       |119.9      |
|25 |Roger Guedes   |10       |119.9      |
|26 |Carla Amorim   |12       |250.0      |
|27 |Eduardo Queiroz|10       |119.9      |
+---+---------------+---------+-----------+
```
- Questão 3
```+---+-------------------------------------+---------+
|id |name                                 |kind     |
+---+-------------------------------------+---------+
|11 |Análise e Desenvolvimento de Sistemas|Tecnólogo|
+---+-------------------------------------+---------+
```
