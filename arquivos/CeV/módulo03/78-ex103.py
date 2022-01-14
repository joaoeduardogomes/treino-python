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
    nome = str("<desconhecido>")

while True:
    try:
        gols = int(input(f"Quantos gols o jogador {nome} marcou? "))
        break
    except ValueError:
        gols = 0
        break

ficha(nome, gols)

# outra alternativa para não ter que usar try/except:
"""
gols = str(input(f"Quantos gols o jogador {nome} marcou? ")) # string pode ficar vazia
if gols.isnumeric():
    gols = int(gols) # aqui se transforma o número de str para numeral int
else:
    gols = 0
"""

# Também é possível passar os parâmetros como opcionais. Nesse caso, se o nome for vazio, só os gols serão passados:
"""
def ficha(nome=<desconhecido>, gols=0)

if nome == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
"""