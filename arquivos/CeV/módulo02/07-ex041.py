"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- até 9 anos = MIRIM
- até 14 anos = INFANTIL
- até 19 anos = JÚNIOR
- até 20 anos = SÊNIOR
- acima dos 20 = MASTER
"""

from datetime import date

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}
categoria = 'MIRIN INFANTIL JÚNIOR SÊNIOR MASTER'.split()

ano_atual = date.today().year
print("Quer descobrir qual sua categoria na Confederação Nacional de Natação?")
ano_nascimento = int(input("Informe sua idade: "))
idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = categoria[0]
elif idade > 9 and idade <= 14:
    categoria = categoria[1]
elif idade > 14 and idade <= 19:
    categoria = categoria[2]
elif idade == 20:
    categoria = categoria[3]
elif idade > 20:
    categoria = categoria[4]

print(f"Com {idade} anos de idade, sua categoria é: {cores['amarelo']}{categoria}{cores['limpa']}.")