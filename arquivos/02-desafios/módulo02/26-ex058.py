"""
Melhore o jogo do desafio 028, em que o computador "pensa" um número entre 0 e 10.
Só que, agora, o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

numero = randint(0, 10)
tentativas = 0

chute = int(input("Pensei em um número de 0 a 10. Você consegue adivinhá-lo? "))

while chute != numero:
    chute = int(input("Você errou. Tente novamente: "))
    tentativas += 1

if chute == numero:
    print(f"Parabéns por ter acertado!\nVocê conseguiu em {tentativas} tentativas.")