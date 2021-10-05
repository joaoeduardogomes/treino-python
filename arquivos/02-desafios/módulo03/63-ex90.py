"""
Faça um programa que leia nome e média de um aluno, guardando também a situação (aprovado/reprovado) em um dicionário. No final, mostre o conteúdo e a estrutura na tela.
"""

resultados = {}

resultados['Nome'] = str(input("Digite o nome do(a) aluno(a): ")).title().strip()
resultados['Média'] = float(input("Digite a média do(a) aluno(a): "))
if resultados['Média'] >= 7:
    resultados['Situação'] = str('Aprovado')
elif 5 <= resultados['Média'] < 7:
    resultados['Situação'] = str('Recuperação')
else:
    resultados['Situação'] = str('Reprovado')

print('-=' * 10)
print("Resultados do(a) aluno(a):")
print('-=' * 10)

for k, v in resultados.items():
    print(f"{k} do(a) aluno(a) = {v}")