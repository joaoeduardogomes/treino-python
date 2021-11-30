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

def cadastraNotas(*num, sit):
    print(num)
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
    escolha_situacao = str(input("Deseja verificar a situação da turma?"))


alunos = [] #aqui vão as informações finais (copiadas do dicionário 'dados')
dados = {} #aqui vão as informações temporárias (copiadas para a lista 'alunos')
notas_aluno = [] #aqui vão todas as notas cadastradas para termos as médias do aluno
notas_turma = [] #aqui vão as notas de toda a turma para o cálculo da média geral
situacao_temporario = []


while True:
    dados.clear()
    notas_aluno.clear()
    while True:
        dados['Nome'] = str(input("Insira o nome do aluno: ")).strip().title()
        if dados['Nome'] != "":
            break

    quant_notas = int(input(f"Quantas notas de {dados['Nome']} gostaria de cadastrar? "))
    for cont in range (0, quant_notas):
        notas_aluno.append(float(input("Informe a nota do aluno: ")))
    cadastraNotas(notas_aluno, sit=True) #O "sit" de "situação" vai ser a opção de mostrar ou não a situação do aluno.

    alunos.append(dados.copy())
    
    '''print(dados)
    print(alunos)
    print(notas_turma)'''
    print(notas_turma)

    escolha_repeticao = str(input("Deseja cadastrar as notas de outro aluno? (s/n) ")).strip().lower()[0]
    while escolha_repeticao not in 'sn':
            escolha_repeticao = str(input("Deseja cadastrar as notas de outro aluno? (s/n) ")).strip().lower()[0]
    if escolha_repeticao == 'n':
        break

while True:
    escolha_exibicao = str(input("Deseja exibir as notas da turma? (s/n) ")).strip().lower()[0]
    if escolha_exibicao == 's':
        exibeDados()
    elif escolha_exibicao == 'n':
        break


'''print(dados)
print(notas)
print(mean(notas)) #mostrar a média da turma'''



'''rascunho: def cadastraNotas():
    while True:
        alunos['Nome'] = str(input("Digite o nome do aluno: ")).strip().title() #add nome

        while True:
            try:
                num_notas = int(input("Quantas notas do aluno deseja cadastrar? "))
                break
            except ValueError:
                continue

        for cont in range(1, num_notas + 1):
            while True:
                try:
                    alunos[f'Nota {cont}'] = float(input(f"Informe a {cont}ª nota do aluno: "))
                    break
                except ValueError:
                    continue
            notas.append(alunos[f'Nota {cont}'])
            situacao_temporario.append(alunos[f'Nota {cont}'])
    
        alunos['Média'] = mean(situacao_temporario) #definir a situação do aluno
        if alunos['Média'] > 7.5:
            alunos['Situação'] = 'Boa'
        elif 6 <= alunos['Média'] <= 7.5:
            alunos['Situação'] = 'Razoável'
        elif alunos['Média'] < 6:
            alunos['Situação'] = 'Ruim'

        dados.append(alunos.copy()) #passar os dados para uma lista definitiva
        
        resposta_cadastro = "a"
        while resposta_cadastro not in 'sn':
            resposta_cadastro = str(input("Deseja cadastrar outro aluno? (s/n) ")).strip().lower()[0]
        if resposta_cadastro == 'n':
            break
'''