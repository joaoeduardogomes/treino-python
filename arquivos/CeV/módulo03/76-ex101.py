"""
Crie um programa que tenha uma função chamada 'voto()', que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando o valor literal indicado se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
** usar aquela biblioteca pra fazer a data de hoje-nascimento e verificar a idade.
**para 16, 17 e 65+ anos o voto é opcional
"""

from time import sleep


def voto(ano_nascimento):
    from datetime import date #importando dentro da função, economiza-se memória
    linhaB('  ANALISANDO SUA SITUAÇÃO  ')
    print(f"{estilo_texto['negrito']}{cor_texto['roxo']}  ANALISANDO SUA SITUAÇÃO  {cor_texto['limpa']}")
    linhaB('  ANALISANDO SUA SITUAÇÃO  ')
    sleep(1.3)
    # cálculo da idade com base no ano de nascimento informado:
    idade = date.today().year - ano_nascimento
    # checagem da condição do voto:
    if idade < 16:
        voto = 'NEGADO'
        cor = cor_texto['vermelho']
    elif 16 <= idade < 18 or idade > 65:
        voto = 'OPCIONAL'
        cor = cor_texto['azul']
    elif 18 <= idade <= 65:
        voto = 'OBRIGATÓRIO'
        cor = cor_texto['verde']
    # resultado na tela:
    print(f"Com {idade} anos, o voto é {cor}{estilo_texto['negrito']}{voto}{cor_texto['limpa']}.")

def linhaA(msg):
    print('~' * len(msg))

def linhaB(msg):
    print('=' * len(msg))

estilo_texto = {'padrão':'\033[0m',
        'negrito' : '\033[1m', 
        'sublinhado':'\033[4m',
        'invertido':'\033[7m',}
cor_texto = {'limpa':'\033[m',
        'branco' : '\033[30m', 
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'ciano' : '\033[36m', 
        'cinza' : '\033[37'}

linhaA('  BEM-VINDO(A) À VERIFICAÇÃO DA SUA CONDIÇÃO DE VOTO  ')
print("  BEM-VINDO(A) À VERIFICAÇÃO DA SUA CONDIÇÃO DE VOTO  ")
linhaA('  BEM-VINDO(A) À VERIFICAÇÃO DA SUA CONDIÇÃO DE VOTO  ')

ano_nascimento = int(input("Informe o ano do seu nascimento: ")) # entrada de dado
voto(ano_nascimento)