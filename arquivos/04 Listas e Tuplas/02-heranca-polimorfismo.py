from abc import ABCMeta, abstractmethod
from functools import total_ordering #importante para fazer <= em objetos. Basta definir os m´petodos "eq" e pelo menos um outro método de comparação.

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

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
            #executa verificação apenas entre contas do tipo 'salário'.
        else:
            return self._codigo == outro._codigo
        #verifica se duas contas são iguais de acordo com o código da conta.
        #A partir de agora, usar "==" ou "!=" funciona de acordo com o critério estabelecido no "eq"

    def __lt__(self, outro): 
        #"lt" = "less than (menos que)"
        return self._saldo < outro._saldo

    def deposita (self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"


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

print('=-' * 30)

conta1 = ContaSalario(37)
print(conta1)

print("~~" * 20)

conta10 = ContaSalario(55)
conta10.deposita(100)

conta11 = ContaSalario(89)
conta11.deposita(200)

print(conta10 <= conta11) #verifica se é menor de acordo com o 'saldo', conforme o método "lt"
# O "==" verifica tando o valor do saldo quanto o código para saber se ambos são iguais. Se ao menos um deles for diferente, não há igualdade.

print()