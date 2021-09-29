"""
Aprimore o desafio anterior(86), mostrando, no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
'''
from time import sleep


valores = [[], [], [], [], []] #ordem: 1ª linha, 2ª linha, 3ª linha, pares, ímpares

for contador in range (1, 4):
    num = int(input(f"Digite um valor para o ponto [1, {contador}]: "))
    valores[0].append(num)
    if num % 2 == 0:
        valores[3].append(num)
    else:
        valores[4].append(num)

for contador in range (1, 4):
    num = int(input(f"Digite um valor para o ponto [2, {contador}]: "))
    valores[1].append(num)
    if num % 2 == 0:
        valores[3].append(num)
    else:
        valores[4].append(num)

for contador in range (1, 4):
    num = int(input(f"Digite um valor para o ponto [3, {contador}]: "))
    valores[2].append(num)
    if num % 2 ==0:
        valores[3].append(num)
    else:
        valores[4].append(num)

print("ANALISANDO OS DADOS...")
sleep(2)

print(f"\nValores digitados: {valores[:3]}")
print(f"Valores pares: {valores[3]}")
print(f"Valores ímpares: {valores[4]}")

print("MONTANDO A MATRIZ...")
sleep(1.5)

for c in valores[0]:
    print(f"[{c:^9}]", end="")
print()
for c in valores[1]:
    print(f"[{c:^9}]", end="")
print()
for c in valores[2]:
    print(f"[{c:^9}]", end="")
print()

print("CALCULANDO OS DADOS...")
sleep(1.5)

print(f"A soma de todos os valores pares é: {sum(valores[3])}")
print(f"A soma de todos os valores da terceira coluna é: {valores[0][2] + valores[1][2] + valores[2][2]}")
print(f"O maior valor da segunda linha é: {max(valores[1])}")

'''

# Alternativa mais curta:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [], []]
soma_coluna = 0

for linha in range (0, 3): #Esta parte é para colocar os valores na lista 'matriz'
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para o ponto [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            matriz[3].append(matriz[linha][coluna])
        else:
            matriz[4].append(matriz[linha][coluna])

print("-=" * 30)
for linha in range (0, 3): #Esta parte é para imprimir os valores na tela
    for coluna in range (0, 3):
        print(f"[{matriz[linha][coluna]:^9}]", end="")
    print() #Este print serve para quebrar uma linha quando o programa terminar de imprimir as colunas

print(f"A soma de todos os valores pares é: {sum(matriz[3])}")
for linha in range (0, 3): #Esta parte é para somar os valores da terceira coluna
    soma_coluna += matriz[linha][2] #A posição da coluna é fixa, só varia a linha
print(f"A soma dos valores da terceira coluna é: {soma_coluna}")
print(f"O maior valor da segunda linha é: {max(matriz[1])}")