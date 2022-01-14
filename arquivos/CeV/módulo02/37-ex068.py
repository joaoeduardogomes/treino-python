"""
Faça um programa em que o usuário jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele acumulou até o final.
"""

from random import randint
from time import sleep

input("Vamos jogar par ou ímpar? O jogo só acaba quando você (usuário) perder uma partida. Pressione ENTER quando estiver pronto: ")

vitorias = 0

opcao = ("par", "ímpar")

while True:
    print("~~"*15)
    escolha = str(input("Escolha se você quer PAR ou ÍMPAR: ")).strip().lower()[0]
    
    while escolha not in "pií":
        escolha = str(input("Escolha inválida. Tente novamente (PAR/ÍMPAR): ")).strip().lower()[0]
    
    if escolha == 'p':
        opcao_usuario = opcao[0]
        opcao_pc = opcao[1]
    elif escolha in 'ií':
        opcao_usuario = opcao[1]
        opcao_pc = opcao[0]
    jogador = int(input("Agora, digite um número INTEIRO qualquer: "))
    pc = randint(0, 10)

    print(f"Você escolheu {opcao_usuario} e jogou o número {jogador}")
    print(f"Eu fiquei com {opcao_pc} e joguei o número {pc}")
    print(f">>> {jogador} + {pc} = {jogador + pc}. O resultado é ", end="")

    if (escolha == 'p' and (jogador + pc) % 2 == 0):
        print("PAR.")
        print("Parabéns, você venceu!")
        vitorias += 1
    elif (escolha in 'ií' and (jogador + pc) % 2 != 0):
        print("ÍMPAR.")
        print("Parabéns, você venceu!")
        vitorias += 1
    else:
        if (jogador + pc) % 2 == 0:
            print("PAR.")
        elif (jogador + pc) % 2 != 0:
            print("ÍMPAR.")
        print("Você perdeu")
        break

    print("~~"*15)
    sleep(2)

print("Fim do programa.")
print(f"Total de vitórias: {vitorias}")