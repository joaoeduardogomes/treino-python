class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Código {self.codigo} Saldo {self.saldo}<<]"

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


print()

conta_caio = ContaCorrente(15)
print(conta_caio)

conta_caio.deposita(500)
print (conta_caio)

print('-' * 30)

conta_ana = ContaCorrente(1684)
conta_ana.deposita(1000)
print(conta_ana)

print('-' * 30)

contas = [conta_caio, conta_ana]
for conta in contas:
    print(conta)

print('~' * 30)

deposita_para_todas(contas)
print(contas[0], contas[1])
