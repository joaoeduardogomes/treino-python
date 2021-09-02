"""
Crie um programa que leia o nome e o preço de vários produtos.
Ele deverá perguntar se o usuário vai continuar passando produtos.
No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1.000,00
c) Qual é o nome do produto mais barato.
"""
from time import sleep

escolha = 's'
produtos = []
valores = []
maisDeMil = 0
menorProduto = ""
menorValor = 0

while escolha == 's':
    print("=-"*20)
    nome = str(input("Informe o nome do produto: "))
    produtos.append(nome)
    sleep(0.5)
    valor = float(input("Informe o valor do produto: R$ "))
    valores.append(valor)
    if valor > 1000:
        maisDeMil += 1
    if menorValor == 0:
        menorProduto = nome
        menorValor = valor
    elif valor < menorValor:
        menorProduto = nome
        menorValor = valor
    sleep(0.5)
    print('~~'*20)

    escolha = str(input("Deseja cadastrar outro produto (S/N)? ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Alternativa inválida. Deseja cadastrar outro produto (S/N)? ")).strip().lower()[0]
    sleep(1)

print("-="*20)
print("ENCERRANDO CADASTRO DE PRODUTOS...")
sleep(1)

print(f"Valor total da compra: R$ {sum(valores):.2f}")
print(f"Sua compra tem {maisDeMil} produto(s) que custa(m) mais de R$ 1000.00")
print(f"O produto de menor valor é '{menorProduto}', que custa R$ {menorValor:.2f}")