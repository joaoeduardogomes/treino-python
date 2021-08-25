# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("Quer saber se três retas podem formar um triângulo? Informe o comprimento de cada uma que eu te digo!")

r1 = float(input("Informe o comprimento da reta 1: "))
r2 = float(input("Informe o comprimento da reta 2: "))
r3 = float(input("Informe o comprimento da reta 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Oba! Parece que temos um triângulo.")    
else:
    print("Não é possível formar um triângulo com as medidas informadas!")