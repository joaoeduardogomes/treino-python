"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior. Os dois são iguais.
"""

print("Me diga dois números inteiros que eu lhe digo qual deles é maior.")
valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
    print(f"O maior número é {valor1}.")
elif valor2 > valor1:
    print(f"O maior número é {valor2}.")
else:
    print("Boa tentativa, mas não conseguiu me enganar! Ambos os valores são iguais.")