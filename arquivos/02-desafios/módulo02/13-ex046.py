# Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0 segundos, com pausa de 1 segundo entre eles.

from time import sleep

cores = {'limpa':'\033[m',
        'azul':'\033[1;40;34m',
        'amarelo':'\033[1;40;33m',
        'vermelho':'\033[1;40;31m',
        'verde':'\033[1;40;32m',
        'roxo':'\033[1;40;35m'}

pintura = ('roxo', 'azul')

str(input("Vamos começar a contagem regressiva para os fogos de artifício. Aperte ENTER quando estiver preparado."))

for contagem in range (10, 0, -1):
    if contagem % 2 == 0:
        num = 1
    else:
        num = 0

    print(f"{cores[pintura[num]]}{contagem}{cores['limpa']}")
    sleep(1)

print(f"{'-='*15}")
print(f"{cores['vermelho']}{'BOOOM!':^30}{cores['limpa']}")
print(f"{'-='*15}")
