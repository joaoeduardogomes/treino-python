"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras. Uma lista vai receber apenas os valores pares e outra apenas os valores ímpares.
Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []
pares = []
impares = []

while True:
    num = int(input("Digite um valor inteiro para adicioná-lo à lista: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)
    escolha = str(input("Deseja adicionar outro valor (S/N)? ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja adicionar outro valor (S/N)? ")).strip().lower()[0]
    if escolha == 'n':
        break
    print(f"Sua lista até o momento: {numeros}")
    print("-="*20)

print("~~"*20)
print(f"Sua lista completa é: {numeros}")
print("-="*20)
print(f"Números pares na lista: {pares}")
print("-="*20)
print(f"Números ímpares na lista: {impares}")
print("-="*20)

# Outra maneira é adicionar os pares e os ímpares por um "for" depois do "while":
"""
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
"""