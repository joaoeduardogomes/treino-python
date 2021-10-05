"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada uma em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres (informar o número também).
D) Uma lista com todas as idades acima da média (informar o número também).
"""

dados = {'nome': "", 'sexo': "", 'idade': 0}
cadastro = []

while True:
    # escolha do número de cadastros:
    while True:
        try:
            quant = int(input("Quantas pessoas deseja cadastrar? "))
            break
        except ValueError:
            print("Por favor, informe um valor numérico.")
            continue
    for cont in range(1, quant+1):
        # inserção do nome:
        while dados['nome'] == "":
            dados['nome'] = str(input("Informe o nome da pessoa: ")).strip().title()
        # inserção do sexo:
        while True:
            try:
                while dados['sexo'] == "" or dados['sexo'] not in 'fm':
                    dados['sexo'] = str(input("Informe o sexo da pessoa: ")).strip.lower()[0]
                break
            except TypeError and AttributeError:
                continue
        # inserção da idade:
        while True:
            try:
                dados['idade'] = int(input("Informe a idade da pessoa: "))
                break
            except ValueError:
                print("Apenas valores numéricos para a idade.")
                continue
        # cópia do dicionário para a lista:
        cadastro.append(dados.copy())
        dados['nome'] = ""
    # opção de cadastrar mais pessoas:
    escolha = str(input("Deseja cadastrar mais pessoas? (S/N) ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja cadastrar mais pessoas? (S/N) ")).strip().lower()[0]
    if escolha == 'n':
        break

print(cadastro)

'''while dados['sexo'] == "" or dados['sexo'] not in 'fm':
            dados['sexo'] = str(input("Informe o sexo da pessoa (M/F): ")).strip().lower()[0]
        if dados['sexo'] == 'm':
            dados['sexo'] = 'masculino'
        elif dados['sexo'] == 'f':
            dados['sexo'] = 'feminino'''