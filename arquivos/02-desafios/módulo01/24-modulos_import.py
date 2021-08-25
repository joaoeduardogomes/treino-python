import math

num = int(input("Digite um número inteiro: "))
raiz = math.sqrt(num)

print(f"A raiz de {num} é igual a {raiz:.2f}.")


# poderia importar apenas a raiz quadrada com: "from math import sqrt"
# Nesse caso, não precisaria usar "math.sqrt(num)", bastaria usar "sqrt.(num)"