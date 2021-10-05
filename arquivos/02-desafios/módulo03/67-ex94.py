"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada uma em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres (informar o número também).
D) Uma lista com todas as idades acima da média (informar o número também).
"""

from time import sleep

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
                    dados['sexo'] = str(input("Informe o sexo da pessoa (M/F): ")).strip().lower()[0]
                break
            except TypeError and AttributeError and IndexError:
                continue
        if dados['sexo'] == 'm':
            dados['sexo'] = 'masculino'
        elif dados['sexo'] == 'f':
            dados['sexo'] = 'feminino'
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
        # Limpando o 'nome' para poder rodar o loop na inserção dele:
        dados['nome'] = ""        
    # opção de cadastrar mais pessoas:
    escolha = str(input("Deseja cadastrar mais pessoas? (S/N) ")).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input("Opção inválida. Deseja cadastrar mais pessoas? (S/N) ")).strip().lower()[0]
    if escolha == 'n':
        break

print("ANALISANDO OS DADOS RECEBIDOS...")
sleep(2)

num_pessoas = len(cadastro) # número de pessoas cadastradas
soma_idades = sum(item['idade'] for item in cadastro) # soma das idades
media_idades = soma_idades / num_pessoas # média das idades

# nº de pessoas e média das idades:
print('-='*30)
print("A) ", end="")
print(f"O número de pessoas cadastradas é: {num_pessoas}")
sleep(1.3)
print()
print("B) ", end="")
print(f"A média das idades do grupo é: {media_idades:5.2f}")
sleep(1.3)
print()

# mulheres cadastradas:
print("C) ", end="")
print("As mulheres da lista são: ")
quant_mulheres = 0
for pessoa in cadastro:
    if pessoa['sexo'][0] in 'f':
        print(f"  — {pessoa['nome']}")
        quant_mulheres += 1
print(f"O total de mulheres é: {quant_mulheres}")
sleep(1.3)
print()

# pessoas com idade acima da média:
print("D) ", end="")
print("As pessoas com idade acima da média são:")
for pessoa in cadastro:
    if pessoa['idade'] > media_idades:
        print("     ")
        for c, v in pessoa.items():
            print(f"{c} = {v}; ", end="")
        print()
print("<< ENCERRADO >>")