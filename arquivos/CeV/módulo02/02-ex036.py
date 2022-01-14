# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário; ou então o empréstimo será negado.

from time import sleep

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'roxo':'\033[1;35m'}

salario = float(input("Informe o seu salário: "))
valor = float(input("Informe o valor do imóvel que deseja comprar: "))
anos = int(input("Informe em quantos anos você pretende quitar o imóvel: "))
meses = anos * 12
parcela = valor / meses

print(f"{cores['roxo']}ANALISANDO SEUS DADOS...{cores['limpa']}")
sleep(3)

if parcela <= salario * 0.3:
    print(f"Parabéns, seu financiamento foi aprovado! \nA parcela do imóvel ficou em {parcela:.2f} por mês durante {anos} anos.")
else:
    print(f"Lamentamos, mas seu financiamento foi negado, pois a parcela é superior a 30% do seu salário. A parcela é R$ {parcela:.2f}, e 30% do seu salário corresponde a R$ {salario * 0.3}")
