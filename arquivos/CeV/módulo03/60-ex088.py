"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 
A) Os números não devem se repetir dentro de um mesmo jogo.
B) Perguntar ao jogador quantos jogos ele quer sortear.
"""

from random import randint
from time import sleep

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}

lista = []
jogos = []

print('-=' * 20)
print('         JOGA NA MEGA SENA         ')
print('=-' * 20)
quant = int(input("Quantos jogos você quer sortear? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3, f" SORTEANDO {quant}JOGOS ", '=-' * 3)
sleep(2)

cor = ''
for indice, lista in enumerate(jogos):
    if indice % 2 == 0:
        cor = 'azul'
    else:
        cor = 'verde'
    print(f"Jogo {indice + 1}: {cores[cor]} {lista} {cores['limpa']}")
    sleep(1.5)

print(f"{cores['roxo']} BOA SORTE NOS SEUS JOGOS!! {cores['limpa']}")