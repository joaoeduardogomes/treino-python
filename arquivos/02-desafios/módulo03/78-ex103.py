"""
Faça um programa que tenha uma função chamada 'ficha()', que receba dois parâmetros opcionais: o 'nome' de um jogador e quantos 'gols' ele marcou.
O programa deverá ser capaz de mostrar a 'ficha do jogador', mesmo que algum dado não tenha sido informado corretamente.
*dica: se o usuário não preencher o nome, o jogador receberá o nome '<desconhecido>'; se não preencher o núemro de gols, será '0'.
"""

def ficha(nome, gols):
    print("-=" * 12, end="")
    print(f"Ficha do jogador {nome}".upper(), end="")
    print("-=" * 12, end=f"\n"*2)
    print(f"Nome = {nome}")
    print(f"Saldo de gols = {gols}", end=f"\n"*2)

nome = str(input("Informe o nome do jogador: ")).strip().title()
if nome == "":
    nome = str("desconhecido").title()

gols = int(input(f"Quantos gols o jogador {nome} marcou? "))

ficha(nome, gols)