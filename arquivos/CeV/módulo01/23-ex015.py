# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Informe a quantidade de dias pelos quais o carro foi alugado: "))
km = float(input("Informe a quilometragem percorrida com o carro: "))

totalDias = dias * 60
totalKm = km * 0.15
total = totalKm + totalDias

print(f"O valor a ser pago é: R${total:.2f}.")