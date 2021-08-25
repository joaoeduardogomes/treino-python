# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = str(input("Insira seu nome completo: ")).strip() #"strip" pra ignorar espaços antes e depois da string
contagem_de_letras = len(nome) - nome.count(" ")

print("Com todas as letras maiúsculas, seu nome fica:", nome.upper())
print("Com todas as letras minúsculas, seu nome fica:", nome.lower())
print("Seu nome completo tem", contagem_de_letras, "letras")
#print(f"Seu primeiro nome tem {nome.find(' ')} letras") #Ele vai encontrar em que parte vem o primeiro espaço vazio. Como vai de 0 a X, a posição do espaço vai ser igual ao número de letras. Ou:
primeiro_nome = nome.split()
print(f"Seu primeiro nome tem {len(primeiro_nome[0])} letras")
