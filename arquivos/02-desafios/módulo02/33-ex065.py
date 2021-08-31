"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o menor e o maior valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

from statistics import mean

lista_numeros = []
cond = True

while cond == True:
    num = int(input("Insira um número inteiro: "))
    lista_numeros.append(num)
    escolha = str(input("Deseja continuar (S/N)? ")).strip().lower()[0]
    if escolha == 'n':
        cond = False
    while escolha != 'n' and escolha != 's':
        escolha = str(input("Opção inválida. Deseja continuar (S/N)? ")).strip().lower()[0]
        if escolha == 'n':
            cond = False
    print('~~'*10)

print(f"Os valores inseridos foram: {lista_numeros}")
print(f"A média entre os valores é: {mean(lista_numeros):.2f}")
print(f"O menor valor inserido foi: {min(lista_numeros)}")
print(f"O maior valor inserido foi: {max(lista_numeros)}")