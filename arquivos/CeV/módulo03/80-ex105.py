"""
Faça um programa que tenha uma função chamada 'notas()", que pode receber várias notas de alunos e retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
    -> as situações são: boa, razoável e ruim
    -> usar algo como 'sit=True'

Adicione também as docstrings da função.
"""

from statistics import mean

def cadastraNotas(*num):
    """
    -> função na qual são cadastradas as notas dos alunos.
    :param *num : todas as notas inseridas no loop.
    """
    for pos in range(0, len(num[0])): #tem que ser "len(num[0]) porque a função cria uma lista dentro de uma tupla"
        dados[f'Nota {pos + 1}'] = num[0][pos]
        
    dados['Menor nota'] = float(min(notas_aluno))
    dados['Maior nota'] = float(max(notas_aluno))
    dados['Média'] = float(mean(notas_aluno))
    if dados['Média'] > 7:
        dados['Situação'] = str('BOA')
    elif 6 <= dados['Média'] <= 7:
        dados['Situação'] = str('RAZOÁVEL')
    elif dados['Média'] < 6:
        dados['Situação'] = str('RUIM')
    notas_turma.append(dados['Média']) #copia-se a média do aluno para depois calcular a média da turma

def exibeDados():
    while True:
        escolha_situacao = str(input("Deseja verificar a situação da turma? (s/n) ")).strip().lower()[0]
        if escolha_situacao == 'n':
            for cont in range(0, len(alunos)):
                del (alunos[cont]['Situação'])
            break
        if escolha_situacao == 's':
            break

    print(alunos)
    print()
    for i, v in enumerate(alunos):
        print(f"{i + 1}: {v}")
    


alunos = [] #aqui vão as informações finais (copiadas do dicionário 'dados')
dados = {} #aqui vão as informações temporárias (copiadas para a lista 'alunos')
notas_aluno = [] #aqui vão todas as notas cadastradas para termos as médias do aluno
notas_turma = [] #aqui vão as notas de toda a turma para o cálculo da média geral


while True:
    dados.clear()
    notas_aluno.clear()
    while True:
        dados['Nome'] = str(input("Insira o nome do aluno: ")).strip().title()
        if dados['Nome'] != "":
            break

    while True:
        try:
            quant_notas = int(input(f"Quantas notas de {dados['Nome']} gostaria de cadastrar? "))
            break
        except ValueError:
            continue
    for cont in range (0, quant_notas):
        notas_aluno.append(float(input("Informe a nota do aluno: ")))
    cadastraNotas(notas_aluno)

    alunos.append(dados.copy())

    escolha_repeticao = str(input("Deseja cadastrar as notas de outro aluno? (s/n) ")).strip().lower()[0]
    while escolha_repeticao not in 'sn':
            escolha_repeticao = str(input("Deseja cadastrar as notas de outro aluno? (s/n) ")).strip().lower()[0]
    if escolha_repeticao == 'n':
        break

while True:
    try:
        escolha_exibicao = str(input("Deseja exibir as notas da turma? (s/n) ")).strip().lower()[0]
    except IndexError:
        continue
    if escolha_exibicao == 's':
        exibeDados()
        break
    elif escolha_exibicao == 'n':
        break