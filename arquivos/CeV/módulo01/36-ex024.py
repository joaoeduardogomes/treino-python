# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Informe o nome da cidade odne você nasceu: ")).strip()
cidade = cidade.lower() #ou testar "in nome.lower()" no teste
cidade = cidade.split()
teste = 'santo' in cidade[0]

if teste == True:
    print("Sua cidade começa com 'Santo'.")
else:
    print("Sua cidade não começa com 'Santo'.")


    # Ao invés do if/else, dá pra testar com "print(cidade[:5].lower() == 'santo')"
