"""
Faça um programa que mostre a tabuada do número solicitado pelo usuário. O programa irá pedir um novo número para mostrar sua respectiva tabuada, e só será interrompido quando o número solicitado for negativo.
"""

from time import sleep

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}


while True:
    print("-="*15)
    num = int(input("Digite um número para saber sua tabuada (números negativos encerram o programa): "))
    
    if num > 0:
        print(f"A tabuada de {num} é:")
        for cont in range (1, 11):
            print(f"{num} x {cont:>2} = {num * cont}")
            sleep(0.2)
    if num < 0:
        break
    sleep(0.5)

print(f"{cores['roxo']}ENCERRANDO...")
sleep(1)
print(f"PROGRAMA ENCERRADO{cores['limpa']}")