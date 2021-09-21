"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

#lista = [[aluno, [nota1, nota2, media]], [aluno, [nota1, nota2, media]]]

resultados = []
dados = []

while True:
    nome = str(input("Insira o nome do aluno: ")).title()
    nota1 = float(input("Insira a 1ª nota do aluno: "))
    nota2 = float(input("Insira a 2ª nota do aluno: "))
    dados.extend([nome, nota1, nota2, (nota1 + nota2) / 2])
    resultados.append(dados[:])
    dados.clear()
    escolha = str(input("Deseja cadastrar outro aluno? (S/N) ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja cadastrar outro aluno? (S/N) ")).strip().lower()[0]
    if escolha == 'n':
        break

print('~~'*60)
print("Nome do aluno                   Média")
print('~~'*60)
for cont in range (0, len(resultados)):
    if cont % 2 == 0:
        print(f"{resultados[cont][0]:.<30}", end="")
    else:
        print(f"{resultados[cont][3]}")
print('-='*60)

print(resultados)