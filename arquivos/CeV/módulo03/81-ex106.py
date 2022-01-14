"""
Faça um mini-sistema que utilize o 'interactive help' do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa será encerrado.

OBS: use cores.
"""
# Não funciona bem no VS code. É melhor usar o PyCharm
from time import sleep

def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'", cor_fundo['azul'])
    print(estilo_texto['invertido'])
    help(com)
    print(cor_texto['limpa'])
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cor, end="")
    print('~' * tam)
    print(f"  {msg}")
    print('~' * tam)
    print(f"{cor_texto['limpa']}", end="")
    sleep(1)


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

cor_fundo = { 'branco' : '\033[40m', 
        'vermelho':'\033[41m',
        'verde':'\033[42m',
        'amarelo':'\033[43m',
        'azul':'\033[44m',
        'roxo':'\033[45m',
        'ciano' : '\033[46m', 
        'cinza' : '\033[47'}

comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP", cor_fundo['roxo'])
    comando = str(input("Função ou Biblioteca > "))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)

titulo("FICAMOS FELIZES EM AJUDAR. VOLTE SEMPRE!", cor_fundo['vermelho'])