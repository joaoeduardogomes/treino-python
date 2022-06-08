import numpy as np

# Os arrays NumPy suportam apenas um tipo por vez. Portanto, devemos fazer uma lista só com int, ou só com float etc.

# criar um array de 0 a 9:
#print(np.arange(10))

#------------------------
'''km = np.array([1000, 2300, 4987, 1500])
print(km)'''

#---------------------------
'''km = np.loadtxt(fname = 'data/carros-km.txt', dtype = int)
print(km)'''

#------------------------
"""dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
acessorios = np.array(dados)
print(acessorios)"""
