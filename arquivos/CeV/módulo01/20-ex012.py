# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valor = float(input("Digite o valor do produto: R$ "))
desconto = valor * 0.95
# Ou: valor - (valor*5/100)

print(f"Com 5% de desconto, o valor fica R$ {desconto:.2f}")
