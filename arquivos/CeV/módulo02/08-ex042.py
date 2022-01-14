"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formadi:
- equilátero = todos os lados iguais
- isóceles = dois lados iguais
- escaleno - todos os lados diferentes
"""

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}

print("Quer saber se três retas podem formar um triângulo? ")
r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))
triangulo = 'EQUILÁTERO ISÓCELES ESCALENO'.split()

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Oba! Parece que temos um triângulo.")
    if r1 == r2 and r1 == r3: # ou: "r1 == r2 == r3"
        triangulo = triangulo[0]
    elif r1 == r2 or r1 == r3 or r2 == r3:
        triangulo = triangulo[1]
    else: #ou: "elif r1 != r2 != r3 != r1" (tem que repetir o r1)
        triangulo = triangulo[2]
    print(f"E ele é do tipo {cores['verde']}{triangulo}{cores['limpa']}")
        
else:
    print(f"{cores['vermelho']}Não é possível formar um triângulo com as medidas informadas!{cores['limpa']}")