"""
Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista nela, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

numeros = []

while True:
    num = int(input("Digite um número inteiro para adicioná-lo a uma lista de valores: "))
    if num not in numeros:
        numeros.append(num)
    else:
        print(f"O número {num} não pôde ser adicionado à lista porque já faz parte dela e está localizado na posição {numeros.index(num)}.")
    escolha = str(input("Quer cadastrar outro número (S/N)? ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja cadastrar outro número (S/N)?")).strip().lower()[0]
    if escolha == 'n':
            break
    print(f"Valores na lista até o momento: {numeros}")
    print("~~"*15)

print(f"A lista completa, em ordem crescente, é: {sorted(numeros)}")