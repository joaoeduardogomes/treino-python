# Crie um programa que leia um número REAL qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

import math

num = float(input("Digite um número real: "))

print(f"A parte inteira de {num} é {math.trunc(num)}")

# Ao invés de importar o "math", uma alternativa é usar "int(num)" no lugar do trunc