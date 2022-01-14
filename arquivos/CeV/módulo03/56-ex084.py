"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves
** O esquemas para os resultados B e C é registrar quais são o menor e o maior pesos registrados. E, a partir disso, dizer quais pessoas têm esse peso.
"""

pessoas = []
dados = []
menor_peso = maior_peso = 0

while True:
    nome = str(input("Informe o nome da pessoa: ")).title()
    dados.append(nome)
    peso = float(input("Informe o peso da pessoa: Kg "))
    dados.append(peso)
    if menor_peso == 0:
        menor_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
    if maior_peso == 0:
        maior_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    pessoas.append(dados[:])
    dados.clear()
    escolha = str(input("deseja cadastrar mais alguém? (S/N) ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja cadastrar mais alguém? (S/N) ")).strip().lower()[0]
    if escolha == 'n':
        break

print(f"Número de pessoas cadastradas: {len(pessoas)}")
print(f"O menor peso é {menor_peso}Kg, de: ", end="")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"[{p[0]}] ", end="")
print()
print(f"O maior peso é {maior_peso}Kg, de: ", end="")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"[{p[0]}] ", end="")
print()




