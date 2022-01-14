"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada (flag).
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

num = 0
numeros = []

while num != 999:
    num = int(input("Digite um número inteiro (ou '999' para terminar o programa): " ))
    if num != 999:
        numeros.append(num)

print(f"Lista de números inseridos: {numeros}.")
print(f"o total de entradas foi: {len(numeros)}")
print(f"A soma de todas as entradas é: {sum(numeros)}")