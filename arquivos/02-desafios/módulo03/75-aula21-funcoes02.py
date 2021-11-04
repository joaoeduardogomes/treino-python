#Todos os códigos abaixo foram explicados no arquivo .docx. Aqui foram digitados apenas para fins de teste prático.

# Interactive Help:
'''
help(print)
help()
print(input.__doc__)
'''

# Docstrings:
'''
def contador (i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}", end="..")
        c += p
    print("FIM!")

help(contador)
'''

# Parâmetros Opcionais:
'''
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f"A soma vale {s}")

somar(3, 2, 5)
somar(8, 4)
somar()'''

# Escopo de variáveis:
'verificar docx'

# Retorno de valores:
'verificar docx'

# parte prática:
'''
def fatorial(num=1): # se 'num' não for especificado, valerá 1 (parâmetro opcional)
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

print('-' * 20)
print("Escolha do usuário:")
n = int(input("Digite um número inteiro: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}") #A segunda chave chama a função.

print('-' * 20)
print("Pré-determinado:")
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são: {f1}, {f2} e {f3}")'''

# retorno de booleano:
def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input("Digite um número inteiro e eu lhe digo se ele é par ou não: "))
if par(num):
    print("É par!")
else:
    print("Não é par!")