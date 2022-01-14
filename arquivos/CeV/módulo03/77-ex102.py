"""
Crie um programa que tenha uma função 'fatorial()' que receba dois parâmetros: o primeiro que indique o NÚMERO a calcular e o segundo chamado SHOW, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial (aquele A x B x C = D).

*dica de como fazer: 'print(fatorial(5, show=True)'
"""

from math import factorial

def fatorial(numero, show=False): #se não preencher, o padrão é falso
    """
    -> Calcula o fatorial de um número.
    :param numero: o número a ter seu fatorial calculado.
    :param show: mostrar ou não a conta.
    """
    fatorial_num = factorial(entrada_num)
    print("-="*20)
    print(f"O fatorial de {entrada_num}! é {fatorial_num}") #aqui mostra só o valor do fatorial
    print("-="*20)

    if show == False:
        escolha = "a"
        while escolha not in 'sn':
            escolha = str(input(f"Deseja ver o fatorial de {entrada_num} em detalhes? (s/n) ")).strip().lower()[0]
            if escolha == 's':
                show = True
            elif escolha == 'n':
                show = False

    # Esta parte irá mostrar todo o processo do fatorial (A x B x C... = valor), caso o usuário decida vê-la.
    if show == True:
        print("-="*20)
        print(f"O fatorial de {entrada_num}! em detalhes é: {entrada_num}", end="")
        for cont in range(entrada_num-1, 0, -1):
            print(f" x {cont}", end="")
        print(f" = {fatorial_num}")
        print("-="*20)


entrada_num = int(input("Digite um número para saber seu fatorial: "))

escolha = "a"
while escolha not in 'sn':
    escolha = str(input(f"Deseja ver o fatorial de {entrada_num} em detalhes? (s/n) ")).strip().lower()[0]
    if escolha == 's':
        mostrar = True
    elif escolha == 'n':
        mostrar = False

fatorial(entrada_num, mostrar)

help(fatorial)