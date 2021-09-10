"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

valoresL = []
paresL = []

for cont in range (1,5):
    num = int(input(f"Digite um valor inteiro ({cont}/4): "))
    valoresL.append(num)
    if num % 2 == 0:
        paresL.append(num)

valoresT = tuple(valoresL)
paresT = tuple(paresL)

print(f"O valor 9 apareceu {valoresT.count(9)} vez(es).")
if 3 in valoresT:
    print(f"O primeiro valor 3 foi digitado na posição {valoresT.index(3)}.")
else:
    print("O valor 3 não foi digitado nenhuma vez.")
print(f"Valores pares digitados: {paresT}")

"""Outra maneira de fazer é:
valoresT = (int(input(f"Digite um valor inteiro: )), 
            int(input(f"Digite um valor inteiro: )), 
            int(input(f"Digite um valor inteiro: )), 
            int(input(f"Digite um valor inteiro: )))
print(f"Você digitou os valores {valoresT}")
"""