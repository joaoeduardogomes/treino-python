"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 
A) Os números não devem se repetir dentro de um mesmo jogo.
B) Perguntar ao jogador quantos jogos ele quer sortear.
"""
#Não funcionou
from random import randint

numeros = []

escolha = 2 #int(input("Quantos sorteios você quer? "))

for cont in range (0, 2):
    while True:
        sorteio = randint(1, 60)
        numeros.append(sorteio)
        print(len(numeros))
        if len(numeros) == 6:
            break

'''while True:
    sorteio = randint(1, 60)
    numeros[0].append(sorteio)
    if len(numeros[0]) == 6:
        break

while True:
    sorteio = randint(1, 60)
    numeros[1].append(sorteio)
    if len(numeros[1]) == 6:
        break'''

print(numeros)