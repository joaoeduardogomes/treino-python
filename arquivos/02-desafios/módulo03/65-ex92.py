"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se, por acaso, a CTPS for diferente de ZERO (não tem), o programa irá perguntar o ano de contratação e o salário; e os adicionará no dicionário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
Considere: para se aposentar é necessário ter 35 anos de contribuição (para fins de resolução deste exercício)
"""

from datetime import date
from time import sleep

dados = {'nome': "", 'ano de nascimento': 0, 'CTPS': 1, 'ano de contratação': 0, 'salário': 0}
cadastro = []

ano_atual = date.today().year

for c in dados:
    if c == 'nome':
        dados[c] = str(input(f"Informe seu {c}: ")).strip().title()
    elif c == 'salário':
        dados[c] = float(input(f"Informe seu {c}: R$ "))
    elif c == 'CTPS':
        dados[c] = int(input(f"Informe seu número de {c} (digite '0' caso não tenha carteira de trabalho): "))
    else:
        dados[c] = int(input(f"Informe seu {c}: "))
    if dados['CTPS'] == 0:
        break
        
dados['idade'] = int(ano_atual - dados['ano de nascimento'])
if dados['CTPS'] != 0:
    dados['idade com que irá se aposentar'] = int(dados['idade'] + 35)

print("ANALISANDO DADOS DO USUÁRIO...")
sleep(1)

for c, v in dados.items():
    if v != 0:
        print(f"{c}: {v}")