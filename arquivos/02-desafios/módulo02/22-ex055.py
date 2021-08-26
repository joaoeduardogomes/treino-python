# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista_pesos = []

for contador in range (1, 6):
    peso = float(input(f"Informe seu peso[{contador}/5]: Kg "))
    lista_pesos.append(peso)

print(f"O maior peso informado foi: {max(lista_pesos)}Kg.")
print(f"O menor peso informado foi: {min(lista_pesos)}Kg.")
