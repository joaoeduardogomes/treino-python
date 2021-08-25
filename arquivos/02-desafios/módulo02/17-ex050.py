# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Dá pra fazer que, se o número for ímpar, o valor da variável dele é 0, e depois mandar somar tudo.

"""n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))
n4 = int(input("Digite um número inteiro: "))
n5 = int(input("Digite um número inteiro: "))
n6 = int(input("Digite um número inteiro: "))

if n1 % 2 != 0:
    n1 = 0
if n2 % 2 != 0:
    n2 = 0
if n3 % 2 != 0:
    n3 = 0
if n4 % 2 != 0:
    n4 = 0
if n5 % 2 != 0:
    n5 = 0
if n6 % 2 != 0:
    n6 = 0

print(f"A soma dos números pares é: {n1+n2+n3+n4+n5+n6}")"""

lista = []

for contador in range (1, 7):
    numero = int(input("Informe um número inteiro: "))
    if numero % 2 != 0:
        numero = 0
    lista.append(numero)

print(f"A soma de todos os números pares informados é: {sum(lista)}")
# É melhor usar "sum(lista)" do que somar manualmente "lista[0] + lista [1] + lista[2] + lista[3] + lista[4] + lista [5]"