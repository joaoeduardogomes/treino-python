"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
- à vista no dinheiro/ débito/pix = 10% de desconto
- à vista no crédito = 5% de desconto
- 2x no crédito = preço normal
- 3x ou mais no crédito = 20% de juros
"""

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}

print(f"{cores['azul']}{'Lojas Glub Glub':=^40}{cores['limpa']}")

valor = float(input("Qual o falor do produto? R$ "))
condicao = int(input("""Qual a condição de pagamento?
[ 1 ] - à vista no dinheiro/débito/pix (10% de desconto)
[ 2 ] - à vista no crédito (5% de desconto)
[ 3 ] - 2x no crédito (valor normal)
[ 4 ] - 3x ou mais no crédito (20% de juros)
Sua escolha: """))

if condicao == 1:
    print(f"O valor à vista fica: {cores['roxo']}R$ {(valor * 0.9):.2f}{cores['limpa']}.")
elif condicao == 2:
    print(f"O valor à vista fica: {cores['roxo']}R$ {(valor * 0.95):.2f}{cores['limpa']}.")
elif condicao == 3:
    print(f"O valor ficou {cores['roxo']}R$ {valor}{cores['limpa']}, a ser pago em 2 parcelas de {cores['amarelo']}R$ {(valor / 2):.2f}{cores['limpa']}.")
elif condicao == 4:
    parcelas = int(input("Em quantas parcelas deseja pagar(máx. 12)? "))
    if parcelas >= 3:
        print(f"O valor ficou {cores['roxo']}R$ {(valor * 1.2):.2f}{cores['limpa']}, a ser pago em {parcelas} parcelas de {cores['amarelo']}R$ {(valor/parcelas):.2f}{cores['limpa']}.")
    else:
        print("Ocorreu um erro. As opções são de 3 a 12 parcelas. Tente novamente.")
else:
    print("Desculpe, as opções são de 1 a 4. Tente novamente")