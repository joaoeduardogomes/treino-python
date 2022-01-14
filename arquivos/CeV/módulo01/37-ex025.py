# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input("Digite seu nome completo: ")).strip()
nome = nome.lower() #ou testar "in nome.lower()" abaixo
teste = 'silva' in nome 

print("Analisando seu nome...")
if teste == True:
    print('Verificamos que há "Silva" no seu nome.')
else:
    print('Verificamos que não há "Silva" no seu nome.')