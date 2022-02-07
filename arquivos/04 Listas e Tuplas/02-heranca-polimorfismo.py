from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass
        #ou usar o erro: raise NotImplementedError
    #Quando a classe-mãe tem um método abstrato, ela dá erro até que esse método seja implementado em todas as classes-filhas.

    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


print()
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

print('-' * 30)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

print('-' * 30)

#conta18 = ContaInvestimento(4156)
#Já dá erro na implementação, porque falta o método abstrato da classe-mãe

print('-' * 30)

contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes()#duck type
    print(conta)


print()