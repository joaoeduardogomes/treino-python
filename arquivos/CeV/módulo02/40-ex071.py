"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (inteiro). O programa irá informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""

print("-="*30)
print(f"{'Banco Qualquer':^60}")
print("-="*30)

valor = int(input("Digite o valor que deseja sacar: R$ "))
total = valor
cedula = 50
totalCed = 0

while True:
    if total >= cedula:
        total = total - cedula
        totalCed += 1
    else:
        if totalCed > 0:
            print(f"Total de {totalCed} cédulas de R$ {cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCed = 0
        if total == 0:
            break
        