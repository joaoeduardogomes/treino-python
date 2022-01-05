def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'polenta'
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    erros = 0

    while (not acertou and not enforcou): #"not acertou" é o mesmo que "acertou = False"
        chute = str(input("Chute uma letra: ")).strip().lower()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6-erros} tentativas.")

        enforcou = erros == 6 #a variável "enforcou" passa a ser verdadeira quando o n° de erros chegar a 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Que pena, você perdeu.")
    print("Fim do jogo")

estilo_texto = {'padrão':'\033[0m',
        'negrito' : '\033[1m', 
        'sublinhado':'\033[4m',
        'invertido':'\033[7m',}

cor_texto = {'limpa':'\033[m',
        'branco' : '\033[30m', 
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'azul':'\033[34m',
        'roxo':'\033[35m',
        'ciano' : '\033[36m', 
        'cinza' : '\033[37'}

cor_fundo = { 'branco' : '\033[40m', 
        'vermelho':'\033[41m',
        'verde':'\033[42m',
        'amarelo':'\033[43m',
        'azul':'\033[44m',
        'roxo':'\033[45m',
        'ciano' : '\033[46m', 
        'cinza' : '\033[47'}

if(__name__ == "__main__"):
    jogar()
