def cria_conta(numero, titular, saldo, limite):
    conta = {"número": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor
    #significa que: conta['saldo'] = conta['saldo'] + valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f"O saldo é: {conta['saldo']}")


conta = cria_conta(1, 2, 3, 4)
print(conta)