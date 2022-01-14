"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma descrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

numeros = []

while True:
    numeros.append(int(input("Digite um valor inteiro para adicioná-lo à lista: ")))
    escolha = str(input("Deseja adicionar outro valor (S/N)? ")).strip().lower()
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja adicionar outro valor (S/N)? ")).strip().lower()[0]
    if escolha == 'n':
        break
    print(f"Sua lista até o momento: {numeros}")
    print('-='*20)

print('~~'*20)
print(f"Quantidade de entradas na lista: {len(numeros)}")
print('-='*20)
numeros.sort(reverse=True)
print(f"A ordem descrescente da lista é: {numeros}")
print('-='*20)
if 5 in numeros:
    print(f"O número 5 faz parte da lista e está localizado na posição {numeros.index(5)}.")
else:
    print("O número 5 não faz parte da lista.")