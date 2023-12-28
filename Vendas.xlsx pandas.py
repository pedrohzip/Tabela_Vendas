import pandas as pd


# importar a base de dados usando a library: pandas
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar os dados usando o library: openpyxl
pd.set_option('display.max_columns', None)
print(tabela_vendas)


# faturamento por loja | Aula: metodos de filtro e agrupamento.
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)


# Desafio: quantidade de produtos vendidos por loja
quantidade_produtos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade_produtos)


# Ticket médio por produto em cada loja                 .to_frame(): transformar em tabela
ticket_medio = (faturamento['Valor Final'] / quantidade_produtos['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)