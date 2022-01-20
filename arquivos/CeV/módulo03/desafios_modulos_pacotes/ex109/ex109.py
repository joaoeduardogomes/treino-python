"""
Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

import moeda


print()
preco = float(input("Digite o preço: R$ "))

taxa1 = 10
taxa2 = 20

print()

print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")

print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")

print(f"Aumentando {taxa1}%, temos {moeda.aumentar(preco, taxa1, True)}")

print(f"Reduzindo {taxa2}% de {preco}, temos {moeda.diminuir(preco, taxa2, True)}")

print()


'''
com o parâmetro True, substituímos o uyso de 'moeda.moeda(moeda.X)', como temos no ex108
'''