"""
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

*Não deve-se alterar o código do 107
"""

import moeda


print()
preco = float(input("Digite o preço: R$ "))

taxa = 10

print()
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"Aumentando {taxa}%, temos {moeda.moeda(moeda.aumentar(preco, taxa))}")
print()

# No 'moeda.moeda', o primeiro moeda é do arquivo .py, o segundo é da def