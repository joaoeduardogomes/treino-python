def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'polenta'
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = str(input("Chute uma letra: ")).strip().lower()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
