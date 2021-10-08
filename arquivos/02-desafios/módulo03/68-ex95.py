"""
Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de jogador.
(é tipo o do boletim escolar)
"""

from time import sleep

jogador = {'nome': "", 'partidas': 0, 'gol(s)': 0, 'gol(s) por partida': 0}
cadastro = []

while True:
    # inserção do nome:
    jogador['nome'] = str(input("Nome do jogador: ")).strip().title()
    if jogador['nome'] == "":
        while jogador["nome"] == "":
            jogador['nome'] = str(input("Por favor, informe o nome do jogador do jogador: ")).strip().title()
    # inserção do nº de partidas do jogador:
    while True:
        try:
            jogador['partidas'] = int(input(f"De quantas partidas o jogador {jogador['nome']} participou? "))
            break
        except ValueError:
            continue
    # inserção do nº de gols por partida do jogador
    if jogador["partidas"] > 0:
        for cont in range (1, jogador["partidas"] + 1):
            while True:
                try:
                    jogador[f'partida {cont}'] = int(input(f"  — Quantos gols o jogador {jogador['nome']} fez na {cont}º partida? "))
                    break
                except ValueError:
                    continue
            # somando o total de gols:
            jogador['gol(s)'] = jogador['gol(s)'] + jogador[f'partida {cont}']
    # calculando a média de gols por partida:
        jogador['gol(s) por partida'] = jogador['gol(s)'] / jogador['partidas']
    # cópia do dicionário para a lista:
    cadastro.append(jogador.copy())
    # zerando o saldo de gols para não interferir no saldo do próximo jogador:
    jogador['gol(s)'] = 0
    # encerramento do programa:
    escolha = str(input("Deseja cadastrar os dados de outro jogador? (S/N) ")).strip().lower()[0]
    while escolha not in "sn":
        escolha = str(input("Opção inválida. Deseja cadastrar os dados de outro jogador? (S/N) ")).strip().lower([0])
    if escolha == 'n':
        break

print('-='*30)
print(f"{'ORGANIZANDO DADOS DOS JOGADORES...':^15}")
sleep(1.5)
print(f"{'Nº':<4}{'NOME':^10}{'MÉDIA DE GOLS POR PARTIDA':>10}")

# mostrar os resultados em tabela:
for i, v in enumerate(cadastro):
    print(f"{i+1:<4}", end="")
    print(f"{cadastro[i]['nome']:^10}", end="")
    print(f"{cadastro[i]['gol(s) por partida']:>10.1f}")
    sleep(0.5)
print()

while True:
    consulta = int(input("Informe o número do jogador do qual gostaria de consultar os detalhes? ('999' para encerrar) ")) -1 #adaptado para poder começar do '1' para o usuário sem bagunçar as chaves da lista.
    if consulta == 999:
        break
    if consulta >= len(cadastro): 
        print(f"Erro! Não há nenhum jogador relacionado ao número {consulta + 1}.") # readaptado para que não mostre um número diferente do que o usuário inseriu (pois foi reduzido '1' logo acima)
    else:
        print(f" —— DETALHES DO JOGADOR {cadastro[consulta]['nome'].upper()}: ")
        for i, v in enumerate(cadastro[consulta].items()):
            print(f"{i}: {v}")
    print('-='*40)

print(" <<< FIM DO PROGRAMA >>>")
print(cadastro)