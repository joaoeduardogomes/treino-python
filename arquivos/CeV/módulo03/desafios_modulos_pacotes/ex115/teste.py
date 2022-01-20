from ex115 import *
from arquivo import *
from time import sleep

print()

arquivo = 'cadastro.txt'

if arquivo_existe(arquivo):
    print("Aqrquivo encontrado!")
else:
    print("Arquivo não encontrado!")

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Realizar novo cadastro', 'Encerrar programa'])
    
    #A resposta recebe o valor 'n' retornado pelo 'inteiro.py'
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print("Encerrando o programa...")
        sleep(0.5)
        break
    else:
        print("Opção inválida!")
        sleep(1)

