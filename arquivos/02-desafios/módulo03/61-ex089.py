"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

#lista = [[aluno, [nota1, nota2], media], [aluno, [nota1, nota2], media]]

resultados = []
dados = []

while True:
    nome = str(input("Insira o nome do aluno: ")).title()
    nota1 = float(input("Insira a 1ª nota do aluno: "))
    nota2 = float(input("Insira a 2ª nota do aluno: "))
    resultados.append([nome, [nota1, nota2], (nota1 + nota2) / 2])
    escolha = str(input("Deseja cadastrar outro aluno? (S/N) ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja cadastrar outro aluno? (S/N) ")).strip().lower()[0]
    if escolha == 'n':
        break

print('-=' * 30)
print(f"{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}")
print('-' * 26)
for indice, aluno in enumerate(resultados):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")


while True:
    print('-=' * 20)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe) "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(resultados) -1:
        print(f"Notas de {resultados[opc][0]} são {resultados[opc][1]}")
print('<<< PROGRAMA FINALIZADO >>>')
