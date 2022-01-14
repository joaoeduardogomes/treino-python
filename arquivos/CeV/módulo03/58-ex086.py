"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta.
"""

'''
valor p/ [1, 1]
valor p/ [1, 2]
valor p/ [1, 3]
valor p/ [2, 1]
valor p/ [2, 2]
valor p/ [2, 3]
valor p/ [3, 1]
valor p/ [3, 2]
valor p/ [3, 3]

Tem que aparecer:
[   x   ] [   x   ] [   x   ]
[   x   ] [   x   ] [   x   ]
[   x   ] [   x   ] [   x   ]
'''

from time import sleep

valores = [[], [], []]

for contador in range (1, 4): # entrada de valores
    valores[0].append(int(input(f"Digite um valor para o ponto [1, {contador}]: ")))

for contador in range (1, 4):
    valores[1].append(int(input(f"Digite um valor para o ponto [2, {contador}]: ")))

for contador in range (1, 4):
    valores[2].append(int(input(f"Digite um valor para o ponto [3, {contador}]: ")))
print("ANALISANDO...")
sleep(2)
print(f"Os valores digitados foram: {valores}.\nMONTANDO A MATRIZ...")
sleep(2)
print("A matriz ficou:")
for c in valores[0]: # montagem da matriz
    print(f" [{c:^9}] ", end="")
print()
for c in valores[1]:
    print(f" [{c:^9}] ", end="")
print()
for c in valores[2]:
    print(f" [{c:^9}] ", end="")


# Alternativa para não precisar usar 'append':
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3): #Esta parte é para colocar os valores na lista 'matriz'
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para o ponto [{linha}, {coluna}]: "))
print("-=" * 30)
for linha in range (0, 3): #Esta parte é para imprimir os valores na tela
    for coluna in range (0, 3):
        print(f"[{matriz[linha][coluna]:^9}]", end="")
    print() #Este print serve para quebrar uma linha quando o programa terminar de imprimir as colunas
'''