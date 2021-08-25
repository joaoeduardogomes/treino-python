"""
Crie um programa que faça o computador jogar jankenpo com você
"""

from random import choice
from time import sleep

cores = {'limpa':'\033[m',
        'azul':'\033[1;40;34m',
        'amarelo':'\033[1;40;33m',
        'vermelho':'\033[1;40;31m',
        'verde':'\033[1;40;32m',
        'roxo':'\033[1;40;35m'}

opcoes = ("pedra", "papel", "tesoura")

entrada = int(input("""Qual sua jogada?
1 - Pedra
2 - Papel
3 - Tesoura
Sua escolha: """))

if entrada == 1:
    jogador = opcoes[0].title()
elif entrada == 2:
    jogador = opcoes[1].title()
elif entrada == 3:
    jogador = opcoes[2].title()
else:
    print("Não tente me enganar! As opções são de 1 a 3.")

computador = choice(opcoes).title()

print(f"{cores['roxo']}JAN")
sleep(1)
print("KEN")
sleep(1)
print(f"PO!!!{cores['limpa']}")
print(f"""{'-=' * 15}
    Jogador:    {jogador}
    Computador: {computador}
{'-=' * 15}""")

if (jogador == computador):
    print(f"{cores['amarelo']}Temos um empate!{cores['limpa']}")
elif jogador == "Pedra":
    if computador == "Tesoura":
        print(f"Pedra esmaga tesoura. {cores['verde']}Você venceu!{cores['limpa']}")
    elif computador == "Papel":
        print(f"Papel enrola pedra. {cores['vermelho']}Você perdeu...{cores['limpa']}")
elif jogador == "Papel":
    if computador == "Pedra":
        print(f"Papel enrola pedra. {cores['verde']}Você venceu!{cores['limpa']}")
    elif computador == "Tesoura":
        print(f"Tesoura corta papel. {cores['vermelho']}Você perdeu...{cores['limpa']}")
elif jogador == "Tesoura":
    if computador == "Papel":
        print(f"Tesoura corta papel. {cores['verde']}Você venceu!{cores['limpa']}")
    elif computador == "Pedra":
        print(f"Pedra esmaga tesoura. {cores['vermelho']}Você perdeu...{cores['limpa']}")
