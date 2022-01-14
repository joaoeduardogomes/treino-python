# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

str(input("Quer saber a soma de todos os números ímpares múltiplos de 3 entre 1 e 500? Aperte ENTER que eu lhe mostro. "))

soma = 0
valores = 0

for contador in range (3, 500, 3):
    if contador % 2 != 0:
        print(contador)
        soma = soma + contador
        valores = valores + 1

print(f"O resultado da soma desses {valores} valores é: {soma}")