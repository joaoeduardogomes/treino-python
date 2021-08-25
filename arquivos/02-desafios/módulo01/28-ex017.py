# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

catetoOposto = float(input("Informe quanto vale o cateto oposto: "))
catedoAdjacente = float(input("Informe quanto vale o cateto adjacente: "))

print(f"A hipotenusa do triângulo é: {math.hypot(catetoOposto, catedoAdjacente):.2f}")
