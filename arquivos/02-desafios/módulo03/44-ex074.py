"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

minha_lista = []

for cont in range (0,5):
    num = randint(0,9)
    minha_lista.append(num)
minha_tupla = tuple(minha_lista)
minha_tupla
#print(minha_lista)
print(f"Os números sorteados foram:{minha_tupla}")
print(f"O menor valor foi {min(minha_tupla)}")
print(f"O maior valor foi {max(minha_tupla)}")

"""Outra maneira mais simples de fazer é:
minha_tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))"""