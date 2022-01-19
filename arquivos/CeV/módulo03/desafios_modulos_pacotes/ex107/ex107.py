"""
Crie um módulo chamado "moeda.py" que tenha as funções incorporadas 'aumentar()', 'diminuir()' e 'metade()'.
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

import moeda

print()
preco = float(input("Digite o preço: R$ "))

taxa = 10

print()
print(f"A metade de R$ {preco:.2f} é R$ {moeda.metade(preco):.2f}")
print(f"O dobro de R$ {preco:.2f} é R$ {moeda.dobro(preco):.2f}")
print(f"Aumentando {taxa}%, temos R$ {moeda.aumentar(preco, taxa):.2f}")
print()
