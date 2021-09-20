"""
Aprimore o desafio anterior(86), mostrando, no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

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
