"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) Quantas pessoas têm mais de 18 anos
b) Quantos homens foram cadastrados
c) Quantas mulheres têm menos de 20 anos
"""

from time import sleep

escolha = 's'
sexo = ' '
menor = homens = mulheres20 = 0

while escolha == 's':
    print("-="*20)
    idade = int(input("Informe a idade da pessoa: "))
    while sexo not in 'mf':
        sexo = str(input("Informe o sexo da pessoa (M/F): ")).strip().lower()[0]
    if idade <= 18:
        menor += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres20 += 1
    sleep(1)
    print("~~"*20)
    escolha = str(input("Deseja cadastrar outra pessoa (S/N)? ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Alternativa inválida. Deseja cadastrar outra pessoa? (S/N)")).strip().lower()[0]
    print("-="*20)
print("ENCERRANDO CADASTROS...")
sleep(2)
print("RESULTADOS:")
print(f"Número de menores de idade cadastrados: {menor}.")
print(f"Número de homens cadastrados: {homens}.")
print(f"Número de mulheres com menos de 20 anos: {mulheres20}.")