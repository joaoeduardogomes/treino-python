"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

termos = int(input("Informe quantos termos da sequência de Fibonacci você deseja ver: "))
cont = 3 #Começa em 3 porque os 2 primeiros termos estão fora do laço
na = 0
nb = 1

print(f"{na} ➝  {nb} ➝  ", end = "")
while cont <= termos:
    n = na + nb
    print(f"{n} ➝  ", end = "")
    na = nb
    nb = n
    cont += 1

print("FIM DO PROGRAMA.")