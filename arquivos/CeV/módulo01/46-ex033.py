# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("Se você me informar três números inteiros, vou tentar descobrir qual deles é o maior e qual é o menor. Vamos começar?")
primeiro = int(input("Informe o primeiro número: "))
segundo = int(input("Informe o segundo número: "))
terceiro = int(input("Informe o terceiro número: "))
maior = 0
menor = 0

if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
elif segundo > primeiro and segundo > terceiro:
    maior = segundo
elif terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print(f"O maior número é: {maior}")

if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
elif segundo < primeiro and segundo < terceiro:
    menor = segundo
elif terceiro < primeiro and terceiro < segundo:
    menor = terceiro
print(f"O menor número é: {menor}")
