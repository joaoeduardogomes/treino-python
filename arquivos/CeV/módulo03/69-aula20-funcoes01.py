'''def mostraLinha(): # é como a "function" do JS.
    print('-' * 30) 
#Deixa-se 2 linhas em branco entre o "def" e o programa principal por questões de organização. Alguns editores de texto notificam se isso não for feito.

mostraLinha() # aqui começa o programa principal
print('     CABEÇALHO     ')
mostraLinha()
mostraLinha()
print('     CORPO     ')
mostraLinha()
mostraLinha()
print('     RODAPÉ     ')
mostraLinha()'''

# definindo o bloco
'''def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem('   ACERVO DE LIVROS   ') #o programa vai substituir o "msg" por cada um dos parâmetros informados em "mensagem" no programa principal
mensagem('   COLEÇÃO DE JOGOS   ')
mensagem('   HQS NA ESTANTE  ')'''

'''# def soma:
def soma(a, b):
    print('-' * 30)
    print(f"a = {a} e b = {b}")
    s = a + b
    print(f"A soma de a + b = {s}")
    print('-' * 30)

soma(4, 5)
soma(8, 9)
soma(a=2, b=1) # É possível explicitar qual valor é qual; inclusive invertendo-os'''

# empacotamento:
"""def contador(*num):
    for valor in num:
        print(f"{valor} ", end="")
    print("FIM")
    tam = len(num)
    print(f"recebi os valores {num} e são, ao todo, {tam} números")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)"""

# outro exemplo:
def soma (* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores}, temos {s}")


soma(5, 2)
soma(2, 9, 4)

# trabalhando com lista (função de dobro):
'''def dobra(lst): # pode ser qualquer nome para o parâmetro, mas foi escolhido "lst"
    pos = 0 # posição
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''