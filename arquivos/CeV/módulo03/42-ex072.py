"""
Crie um programa que tenha uma tupla totalmente preenchida com números por extenso, de 0 a 20.
Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso.
"""

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    entrada = int(input("Digite um número de 0 a 20: "))

    while entrada > 20 or entrada < 0:
        entrada = int(input("Valor inválido. Por favor, digite um número de 0 e 20: "))

    print(f"Você escolheu o número {num[entrada]}.")
    escolha = str(input("Quer continuar? ")).strip().lower()
    if escolha == 'n':
        break
    elif escolha not in 'sn':
        escolha = str(input("Opção inválida. Quer continuar? ")).strip().lower()
        if escolha == 'n':
            break