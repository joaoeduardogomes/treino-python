# Contando a recorrência de palavras num texto:

from collections import Counter


meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

'''
aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
'''


#Maneira mais fácil, usando o "counter":
aparicoes = Counter(meu_texto.split())

for c, v in aparicoes.items():
    print(f"{c} = {v}")