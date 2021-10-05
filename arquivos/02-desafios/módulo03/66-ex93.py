"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
    *NOTA1: O programa vai perguntar quantas partidas o jogador jogou. Depois, vai perguntar quantos gols ele marcou em cada partida.
    *NOTA2: se o jogador não esteve em nenhuma partida, o programa não deve perguntar o número de gols marcados.
"""

from time import sleep

dados = [{'nome': ""}, {'partidas': 0, 'gols': 0, 'gol(s) por partida': 0}]

dados[0]['nome'] = str(input("Digite o nome do jogador: ")).strip().title()

dados[1]['partidas'] = (int(input(f"Quantas partidas [{dados[0]['nome']}] jogou? ")))

for cont in range (1, dados[1]['partidas']+1):
    dados[1][f'partida {cont}'] = int(input(f"Quantos gols [{dados[0]['nome']}] marcou no jogo {cont}? "))
    # Adicionando o saldo total de gols na chave 'gols':
    dados[1]['gols'] = dados[1]['gols'] + dados[1][f'partida {cont}']

dados[1]['gol(s) por partida'] = dados[1]['gols'] / dados[1]['partidas']

print('-='*15)
print(f"APROVEITAMENTO DO JOGADOR {dados[0]['nome'].upper()}:")
print('-='*15)
sleep(1.5)

for c, v in dados[1].items():
    print(f"{c.title()}: {v:.2f}")