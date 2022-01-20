def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.') #troca a vírgula por ponto pro número com vírgula também ser aceito
        if entrada.isalpha() or entrada.strip() == '':
            print(f"ERRO! \"{entrada}\" é um valor inválido!")
        else:
            valido = True
            return float(entrada)


