"""
Dentro de um pacote 'utilidadesCeV', que criamos no desafio 111, temos um módulo chamado 'dado'. Crie uma função chamada 'leiaDinheiro()' que seja capaz de funcionar como a função 'input()', mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

from utilidadescev import moeda, dado

print()
preco = dado.leia_dinheiro("Digite o preço: R$ ")


print()

moeda.resumo(preco, 15, 30)

print()