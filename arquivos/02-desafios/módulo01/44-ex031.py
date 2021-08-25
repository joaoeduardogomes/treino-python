# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

km = float(input("Informe a distância em Km da viagem que você quer fazer para saber o valor da passagem: "))

if km <= 200:
    print(f"O valor da passagem será R${km * 0.5:.2f}.")
else:
    print(f"O valor da passagem será R$ {km * 0.45:.2f}.")
