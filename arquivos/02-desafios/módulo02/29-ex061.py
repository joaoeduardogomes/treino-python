"""
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

termo1 = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
termo = termo1
contador = 1

print("A PA é:")
while contador <= 10:
    print(f"{termo} ", end = "")
    termo = termo + razao
    contador += 1
