"""
Faça um valor que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

numeros = []

for cont in range (0, 5):
    numeros.append(int(input(f"Digite um número inteiro para a posição {cont}: ")))
    print("-="*10)

maior = max(numeros)
menor = min(numeros)

print(f"Os números inseridos foram: {numeros}")
print("-="*10)
print(f"O maior número inserido foi {maior}, que está posicionado no(s) espaço(s): ", end="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor número inserido foi {menor}, que está posicionado no(s) espaço(s): ", end="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i}...", end="")
print()
print(f"Na ordem, a lista fica: {sorted(numeros)}")
print("-="*10)



# Este abaixo funciona, mas só mostra a primeira posição em que aparece o menor e o maior números:
"""print(f"O maior número inserido foi {maior}, na posição {numeros.index(maior)} da lista.")
print("-="*10)
print(f"O menor número inserido foi {menor}, na posição {numeros.index(menor)} da lista.")
print("-="*10)"""