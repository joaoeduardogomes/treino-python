"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores, dizer quantos valores foram inseridos, mostrá-los e dizer qual deles é o maior.
"""

from random import randint

def maior(*num):
    print('~~' * 20)
    print(f"os números sorteados foram: {sorted(valores)}")
    print(f"Ao todo, foram sorteados {len(valores)} valores")
    print(f"O maior valor é: {max(valores)}")
    print('~~' * 20)


valores = []
num = int(input("Quantos valores deseja sortear? "))
for cont in range (0, num):
    valores.append(randint(1, 10))
maior(valores)