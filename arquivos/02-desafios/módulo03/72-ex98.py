"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: INÍCIO, FIM e PASSO e realize a contagem.

Seu programa tem que realizar TRÊS CONTAGENS através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, voltando de 2 em 2
c) Uma contagem personalizada ( o usuário informa)
    atenção a entradas negativas e 0 para o passo.
"""

from time import sleep

def contador(inicio, fim, passo):
    print('-' * 20)
    if inicio > fim and passo > 0:
        passo = -passo
    if passo == 0:
        passo = 1
    for cont in range(inicio, fim, passo):
        print(f"{cont} ", end="")
    print()
    print('-' * 20)


contador(1, 10, 1)
contador(10, 0, 2) # se colocar "-2" no passo funciona igual por causa do primeiro "if" na função.

inicio = int(input("Informe o número inicial (inteiro): "))
fim = int(input("Informe o número final (inteiro): "))
passo = int(input("Informe o passo (inteiro): "))
contador (inicio, fim, passo)