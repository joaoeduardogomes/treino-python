# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

for contador in range (3, 500, 3):
    if contador % 2 != 0:
        print(contador)
        