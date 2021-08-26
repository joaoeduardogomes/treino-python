# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}

num = int(input("Digite um número inteiro e eu lhe digo se ele é primo ou não: "))

multiplos = 0

print("Múltiplo de:")
for contador in range (1, num + 1):
    if num % contador == 0:
        print(f"{contador}")
        multiplos = multiplos + 1

print(f"{cores['verde']}-="*20, f"{cores['limpa']}")
print(f"O número {num} foi divisível {multiplos} vezes")
if multiplos == 2:
    print(f"Logo, {num} é um número primo!")
else:
    print(f"Logo, {num} não é um número primo.")
print(f"{cores['verde']}-="*20, f"{cores['limpa']}")