# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Dá pra fazer que, se o número for ímpar, o valor da variável dele é 0, e depois mandar somar tudo.

lista = []
numeros_pares = 0

for contador in range (1, 7):
    numero = int(input(f"Digite um número inteiro [{contador}/6]: "))
    if numero % 2 == 0:
        numeros_pares += 1
        lista.append(numero)

print(f"Você informou {numeros_pares} número(s) par(es). E a soma total é: {sum(lista)}.")
# É melhor usar "sum(lista)" do que somar manualmente "lista[0] + lista [1] + lista[2] + lista[3] + lista[4] + lista [5]"