"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
- média abaixo de 5.0 = reprovado
- média entre 5.0 e 6.9 = recuperação
- média 7.0 ou superior = aprovado
"""

from time import sleep

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}
print("Vamos verificar se um aluno tem média para ser aprovado?")
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

print(f"{cores ['roxo']}CALCULANDO...{cores['limpa']}")
sleep(3)

if media >= 7:
    print(f"Parabéns! Sua média foi {cores['verde']}{media:.1f}{cores['limpa']} e você está aprovado")

elif media >= 5 and media < 7: #ou "7 > media >= 5"
    print(f"Foi quase! Mas, com média {cores['amarelo']}{media:.1f}{cores['limpa']}, você está de recuperação.")
elif media < 5:
    print(f"Infelizmente sua média foi {cores['vermelho']}{media:.1f}{cores['limpa']} e você está reprovado. Esforce-se mais no próximo ano!")
