"""
Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~ (Isso aqui tem que ter largura de acordo com a entrada, talvez usando "len")
Olá, Mundo!
~~~~~~~~~~~~~
"""

def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f"  {msg}")
    print('~' * tamanho)


mensagem = str(input("Digite algo: "))
escreva(mensagem)