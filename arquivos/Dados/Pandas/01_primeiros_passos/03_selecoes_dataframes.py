import pandas as pd

dataset = pd.read_csv('data/db.csv', sep = ';', index_col = 0) # o terceiro parâmetro indica que a coluna 0 (nome) será usada como index, ao invés do padrão numérico gerado pelo Pandas.

#print(dataset.head()) # pega só as 5 primeiras colunas

#print(dataset.loc['Passat'])

