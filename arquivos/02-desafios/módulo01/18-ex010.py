# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Dólar em 04/08/2021 = R$ 5,19

nReal = float(input("Informe o valor que você tem em reais: "))
nDolar = nReal / 5.19

print(f"Com R${nReal} você pode comprar USD{nDolar}.")
