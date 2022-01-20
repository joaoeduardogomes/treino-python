"""
Crie umn pacote chamado 'utilidadesCeV' que tenha dois módulos internos chamados 'moeda' e 'dado'.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""

from utilidadescev import moeda

print()
preco = float(input("Digite o preço: R$ "))


print()

moeda.resumo(preco, 15, 30)

print()