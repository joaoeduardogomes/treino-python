from random import randrange


def define_palavra():
    # Abrindo o .txt para palavras aleatórias
    arquivo = open("forca_palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip() #isso vai tirar o "\n" da quebra de linha
        palavras.append(linha)

    arquivo.close() #fechando a leitura do .txt

    numero = randrange(0, len(palavras)) #escolhendo uma palavra aleatoriamente. Usa-se "randrange" porque o número final é ignorado. Isso é importante porque o último item da lista é um número menor do que o tamanho dela (porque começa em 0).

    palavra_secreta = palavras[numero].upper() #definindo a palavra secreta

    return palavra_secreta #permite que a variável seja acessada fora da função

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = str(input(f"\nChute uma letra: ")).strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def jogar():
    mensagem_abertura()

    palavra_secreta = define_palavra()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False

    print(letras_acertadas)

    erros = 0

    while (not acertou and not enforcou): #"not acertou" é o mesmo que "acertou = False"
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1
            print(f"\nOps, você errou! Faltam {6-erros} tentativas.")
            desenha_forca(erros)


        enforcou = erros == 7 #a variável "enforcou" passa a ser verdadeira quando o n° de erros chegar a 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vitoria(palavra_secreta)
    else:
        imprime_mensagem_derrota(palavra_secreta)
    print("Fim do jogo")

def imprime_mensagem_vitoria(palavra_secreta):
    print(f"\nParabéns, você ganhou!")
    print(f"A palavra foi: {palavra_secreta.title()}")
    print(f"{cor_texto['amarelo']}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print(f"{cor_texto['limpa']}")

def imprime_mensagem_derrota(palavra_secreta):
    print(f"\nQue pena, você perdeu.")
    print(f"A palavra era: {palavra_secreta.title()}")
    print(f"{cor_texto['vermelho']}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print(f"{cor_texto['limpa']}")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


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
