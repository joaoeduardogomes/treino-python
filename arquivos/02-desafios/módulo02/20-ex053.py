# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

cores = {'limpa':'\033[m',
        'azul':'\033[1;40;34m',
        'amarelo':'\033[1;40;33m',
        'vermelho':'\033[1;40;31m',
        'verde':'\033[1;40;32m',
        'roxo':'\033[1;40;35m'}

frase = str(input("Digite uma frase e eu lhe digo se ela é um palíndromo: ")).lower()
reverso = frase[::-1]


if frase.replace(" ", "") == reverso.replace(" ", ""):
    print(f"A frase digitada {cores['verde']}é um palíndromo!{cores['limpa']}")
    print(f"Resultado: {cores['roxo']}{reverso}{cores['limpa']}")
else:
    print(f"A frase digitada {cores['vermelho']}não é um palíndromo{cores['limpa']}.")
    print(f"Resultado: {cores['roxo']}{reverso}{cores['limpa']}")
