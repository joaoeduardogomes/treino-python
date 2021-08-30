"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1=120
"""

num = int(input("Informe um número inteiro para saber seu fatorial: "))
fatorial = num
print(num, end="")
while (num-1) >= 1:
    print(f"x{num-1}", end="")
    num -= 1
    fatorial = fatorial * num
print(f" = {fatorial}")