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
    if inicio > fim and passo > 0: #A contagem regressiva funciona com passo positivo ou negativo
        passo = -passo
    if inicio < fim and passo < 0: #A contagem padrão funciona com passo positivo ou negativo
        passo = -passo
    if passo == 0: #Se o passo inserido for 0, ele é convertido para 1
        passo = 1

    for cont in range(inicio, fim+passo, passo):
        print(f"{cont} ", end="", flush=True) #esse "flush" é uma espécie de buffer de tela. Com ele desativado, o programa executa com o sleep mas só imprime na tela quando termina a contagem.
        #sleep(0.3)
    print('FIM!')
    print()
    print('-' * 20)


contador(1, 10, 1)
contador(10, 0, 2) # se colocar "-2" no passo funciona igual por causa do primeiro "if" na função.

print("A próxima contagem é você quem faz!")
#sleep(1)
inicio = int(input("Informe o número inicial (inteiro): "))
fim = int(input("Informe o número final (inteiro): "))
try: #Aqui, se a entrada for vazia ou inválida (como uma letra), o passo será convertido para 1
    passo = int(input("Informe o passo (inteiro): "))
except ValueError:
    passo = 1
contador (inicio, fim, passo)