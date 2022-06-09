import pandas as pd

'''impportando os dados:'''
dados = pd.read_csv('aluguel.csv', sep = ";")

#print(dados.head())

#-------------------------------

'''INFORMAÇÕES GERAIS SOBRE OS DADOS:'''
#print(dados.dtypes)

#tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])
#tipos_de_dados.columns.name = 'Variáveis'
#print(tipos_de_dados)

#print(f"A base de dados apresenta {dados.shape[0]} registros (imóveis) e {dados.shape[1]} variáveis.")