# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número inteiro e eu lhe digo se ele é primo ou não: "))

multiplos = 0

for contador in range (2, num):
    if num % contador == 0:
        print(f"Múltiplo de {contador}")
        multiplos = multiplos + 1

if multiplos == 0:
    print(f"{num} é um número primo!")
else:
    print(f"{num} não é um número primo.")