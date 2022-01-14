"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
- A média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos"""

from statistics import mean #importando o cálculo de média

media_idade = []
maior_idade_homem = 0
homem_mais_velho = ""
mulheres_20 = []

for contador in range (1, 5):
    print(f"----- {contador}ª PESSOA -----")
    nome = str(input("Informe seu nome: ")).strip().title()
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Qual seu sexo? (M/F) ")).strip().lower()
    media_idade.append(idade)
    if (sexo != 'm' and sexo != 'f') and (sexo != 'masculino' and sexo != 'feminino'):
        print("Alternativa de sexo inválida.")
    if (sexo == 'm' or sexo == 'masculino') and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    if (sexo == 'f' or sexo == 'feminino') and idade < 20:
        mulheres_20.append(idade)

print(f"A media da idade do grupo é {mean(media_idade):.2f}")
print(f"O nome do homem mais velho é: {homem_mais_velho}")
print(f"O número de mulheres com menos de 20 anos é: {len(mulheres_20)}")