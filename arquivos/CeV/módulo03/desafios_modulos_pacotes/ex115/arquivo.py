from ex115 import *

def arquivo_existe(nome):
    try:
        a = open(nome, encoding='utf-8', mode='rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cria_arquivo(nome):
    try:
        a = open(nome, encoding='utf-8', mode='wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso.")

def le_arquivo(nome):
    try:
        arquivo = open(nome, encoding='utf-8', mode='rt')
    except:
        print("Erro na leitura do arquivo.")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(arquivo.read())
    finally:
        arquivo.close()

def cadastra(arquivo, nome = 'desconhecido', idade = 0):
    try:
        arquivo = open(arquivo, encoding='utf-8', mode='at')
    except:
        print("ERRO! O arquivo não pôde ser aberto.")
    else:
        try:
            arquivo.write(f"{nome}, {idade}\n")
        except:
            print("Erro no cadastro de dados.")
        else:
            print(f"{nome} cadastrado(a) com sucesso!")
            arquivo.close()