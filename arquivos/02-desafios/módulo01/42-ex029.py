# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

km = int(input("Informe a quantos Km/h você estava: "))

if km > 80:
    print(f"O limite de velocidade é 80Km/h. Você foi multado em R$ {(km-80) * 7},00.")
else:
    print("Ufa! Você não foi multado! A velocidade máxima é de 80Km/h.")
