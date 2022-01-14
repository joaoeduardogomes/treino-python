# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Informe um ângulo para descobrir seu seno e cosseno: "))

print(f"O seno de {angulo}° é {math.sin(math.radians(angulo)):.2f}. \nO cosseno de {angulo}° é {math.cos(math.radians(angulo)):.2f}. \n E a tangente de {angulo}° é {math.tan(math.radians(angulo)):.2f}.")