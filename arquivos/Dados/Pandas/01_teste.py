import pandas as pd

dataset = pd.read_csv('data/db.csv', sep = ';') # 'sep' é o separador
pd.set_option('display.max_rows', 300) #mostra todas as linhas (segundo param. é o máx.)
pd.set_option('display.max_columns', 10) # mostra todas as colunas (segundo param. é o máx.)
#print(dataset)

#print(dataset[['Quilometragem', 'Valor']].describe())

#print(dataset.info())