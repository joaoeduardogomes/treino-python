# crie um programa que leia um ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (maioridade = 21 anos)
# Fazer um laço pra ficar perguntando a idade. Colocar um "if" que, sempre que uma pessoa for de maior, soma na variável MAIOR, e sempre que for de menor, soma na variável MENOR.

from datetime import date

anos = [] #Aqui estabelece que vai existir uma lista
ano_atual = date.today().year
menor = 0
maior = 0

for contador in range (1, 8):
    ano =  int(input(f"informe seu ano de nascimento [{contador}/7]: "))
    anos.append(ano)
    if ano_atual - ano < 21:
        menor = menor +1
    elif ano_atual - ano >= 21:
        maior = maior +1

print(f"Das pessoas informadas, {menor} é(são) menor(es) de idade.\nE {maior} é(são) maior(es) de idade.")