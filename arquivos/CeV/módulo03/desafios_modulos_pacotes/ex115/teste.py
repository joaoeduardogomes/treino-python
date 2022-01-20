from ex115 import *
from arquivo import *
from inteiro import *
from time import sleep

print()

arquivo = 'cadastro.txt'

if not arquivo_existe(arquivo):
    cria_arquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Realizar novo cadastro', 'Encerrar programa'])
    
    #A resposta recebe o valor 'n' retornado pelo 'inteiro.py'
    if resposta == 1:
        le_arquivo(arquivo)
        sleep(1)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastra(arquivo, nome, idade)
        sleep(1)
    elif resposta == 3:
        print("Encerrando o programa...")
        sleep(0.5)
        break
    else:
        print("Opção inválida!")
        sleep(1)

