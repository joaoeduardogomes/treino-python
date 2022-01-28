from random import randint


def cria_conta(numero, titular, saldo, limite):
    conta = {"número": numero, "titular": titular, "saldo": saldo, "limite": limite}

    conta['número'] = int(randint(123, 999))
    print(conta)
    return conta


