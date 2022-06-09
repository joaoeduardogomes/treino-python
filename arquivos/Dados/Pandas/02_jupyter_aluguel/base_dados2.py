import pandas as pd

'''TIPOS DE IMÓVEIS'''
dados = pd.read_csv('aluguel.csv', sep = ";")
dados.head(10)

tipos_de_imovel = dados['Tipo']

