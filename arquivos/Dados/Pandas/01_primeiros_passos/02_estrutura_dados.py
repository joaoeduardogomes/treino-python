import pandas as pd

# Dados internos:
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

'''dataset = pd.DataFrame(dados)
pd.set_option('display.max_columns', 10) 
print(dataset)'''

''' Se quisermos alterar a ordem de impressão:
dataset[['Nome', 'Motor', 'Ano', 'Quilometragem', 'Zero_km', 'Valor']]
'''

#--------------------------
# Dados externos:
dataset = pd.read_csv('data/db.csv', sep = ';')
print(dataset)