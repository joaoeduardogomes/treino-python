# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep # o "sleep" é uma funcionalidade que faz o programa "dormir" por um tempo determinado

numero_pensado = randint(0, 5)
numero = int(input("Pensei em um número entre 0 e 5. Você consegue adivinhá-lo? "))

print("\033[1;31;43mPROCESSANDO...\033[m") #Aqui fiz um teste com cores
sleep(3) #aqui ele pausa por 3 segundos antes de prosseguir

if numero == numero_pensado:
    print("Parabéns, você acertou!")
else:
    print(f"Você errou! O número pensado foi {numero_pensado}")
