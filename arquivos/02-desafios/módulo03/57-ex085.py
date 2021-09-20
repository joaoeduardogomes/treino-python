"""
Crie um programa em que o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
# Testar se funciona:
numeros = [[], []]

for contador in range (1, 8):
    num = int(input(f"Digite um número inteiro ({contador}/7): "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1]. append(num)

print(f"Os números pares digitados foram: {sorted(numeros[0])}")
print(f"Os números ímpares digitados foram: {sorted(numeros[1])}")