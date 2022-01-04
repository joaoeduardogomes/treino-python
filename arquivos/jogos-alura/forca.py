def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'polenta'

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):
        chute = str(input("Chute uma letra: ")).strip().lower()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print(f"Encontrei a letra {letra} na posição {index}")
            index += 1
        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
