"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu resultado de acordo com a tabela abaixo:
- abaixo de 18.5 = abaixo do peso
- entre 18.5 e 25 = peso ideal
- 25 até 30 = sobrepeso
- 30 a 40 = obesidade
- acima de 40 = obesidade mórbida
"""

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'roxo':'\033[1;35m'}

print("Vamos descobrir como está seu IMC?")
altura = float(input("Informe sua altura em metros: "))
peso = float(input("Informe seu peso em quilogramas: "))

imc = peso / (altura**2)

print(f"Seu IMC é {cores['roxo']}{imc:.1f}{cores['limpa']}.")

if imc < 18.5:
    print(f"Você está {cores['azul']}abaixo do peso{cores['limpa']}.")
elif imc >= 18.5 and imc < 25:
    print(f"Você está no seu {cores['verde']}peso ideal{cores['limpa']}. {cores['roxo']}Parabéns!{cores['limpa']}")
elif imc >= 25 and imc < 30:
    print(f"Você está com {cores['amarelo']}sobrepeso{cores['limpa']}.")
elif imc >= 30 and imc <= 40:
    print(f"Você é considerado {cores['vermelho']}obeso{cores['limpa']}. Cuide-se melhor!")
else:
    print(f"Você tem {cores['vermelho']}obesidade mórbida{cores['vermelho']}. Precisa se cuidar urgentemente!")
    