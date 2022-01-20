def leiaInt(valor):
    while True:
        try:
            print('~~' * 20)
            n = int(input(valor))
            print('~~' * 20)
            break
        except ValueError:
            print(f"ERRO! Opção não disponível.")
            continue

    return n