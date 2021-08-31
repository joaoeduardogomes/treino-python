"""
Melhore o jogo do desafio 028, em que o computador "pensa" um número entre 0 e 10.
Só que, agora, o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

numero = randint(0, 10)
tentativas = 1

chute = int(input("Pensei em um número de 0 a 10. Você consegue adivinhá-lo? "))

while chute != numero:
    tentativas += 1
    if chute < numero:
        chute = int(input("Errado! O número é maior do que esse... "))
    elif chute > numero:
        chute = int(input("Errado! O número é menor do que esse... "))    
        
if chute == numero:
    print(f"Parabéns por ter acertado!\nVocê conseguiu em {tentativas} tentativa(s).")