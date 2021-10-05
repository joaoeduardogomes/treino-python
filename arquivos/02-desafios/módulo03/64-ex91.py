"""
Crie um programa em que 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
Na prática, ele tem que mostrar o resultado de cada jogador. Depois, tem que mostrar um ranking com a classificação de cada jogador e seu respectivo resultado no dado.
"""

from random import randint
from operator import itemgetter
from time import sleep

jogos = [{'nome': 'Jogador 1', 'resultado': 0 }, {'nome': 'Jogador 2', 'resultado': 0}, {'nome': 'Jogador 3', 'resultado': 0}, {'nome': 'Jogador 4', 'resultado': 0}]

print('-='*15)
for cont in range (0, 4):
    jogos[cont]['resultado'] = randint(1, 20)
    print(f"Resultado do Jogador {cont+1}: {jogos[cont]['resultado']}")
    print('-='*15)
    sleep(1.5)

print("ORGANIZANDO O RANKING...")
sleep(3)
rank = sorted(jogos, key=itemgetter('resultado'), reverse=True) #Aqui é feita a organização com base no item 'resultado' dos dicionários. O 'reverse=True' estabelece que será do maior pro menor. 'rank' é uma lista.

print('~~'*15)
for c, v in enumerate(rank):
    print(f"  — Em {c+1}º lugar ficou o {v['nome']}, com o resultado {v['resultado']}")
    sleep(1.5)

print('~~'*15)


#Rascunho:
'''jogos = [{'Jogador 1': 0 }, {'Jogador 2': 0}, {'Jogador 3': 0}, {'Jogador 4': 0}]

for cont in range (0, 4):
    jogos[cont][f'Jogador {cont+1}'] = randint(1, 20)
    print(f"Resultado do Jogador {cont+1}: {jogos[cont][f'Jogador {cont+1}']}")

print('-='*15)
for k, v in enumerate(jogos):
    print(f"{k}, {v}")
print('-='*15)'''