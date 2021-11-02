"""
Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas SORTEIA() e SOMApAR(). A primeira função vai sortear 5 NÚMEROS e vai colocá-los dentro da lista. A segunda função vai mostrar a SOMA entre todos os valores PARES sorteados pela função anterior.
"""

from random import randint

def sorteia():
    print('-=' * 20)
    for cont in range(0, 5):
        numeros.append(randint(1, 20))
    print(f"Os números sorteados foram: {sorted(numeros)}")
    print('-=' * 20)

def somaPar():
    print('=-' * 20)
    soma = sum(num for num in numeros if num%2==0) # Esta parte vai somar só os pares, isto é, aqueles que tem resto 0 na divisão inteira por 2.
    #original era: "sum(num for num in numeros if num%2==0)"
    print(f"A soma de todos os números pares da lista é: {soma}")
    print('=-' * 20)


numeros = []

sorteia()
somaPar()