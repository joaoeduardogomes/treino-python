'''
Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: 
    1) cadastrar uma nova pessoa
    2) listar todas as pessoas cadastradas
'''
from inteiro import leiaInt
# "*" = importar tudo o que tem na biblioteca

def linha( tam = 42):
    return '-' * tam

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabecalho('INÍCIO | CADASTROLL')

    cont = 1
    for item in lista:
        print(f"{cont} — {item}")
        cont += 1
        
    print(linha())

    opcao = leiaInt('Sua escolha: ')
    return opcao