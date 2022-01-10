from datas import Data

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto...{self}")
        #O self será o código do objeto. Ele é a referência do objeto criado.
        """
        Basta seguir o passo a passo no console:
        1) "from b_conta import Conta"
        2) conta = Conta()
        """
        #Os valores abaixo podem tanto ser especificados após o ponto como serem introduzidos pelo usuário. Para o segundo caso, basta pedir esses parâmetros no "def" e colocá-los no "self" abaixo.
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}")
        print("Data do extrato: ", end="")
        Data()

    def deposita(self, valor):
        self.saldo += valor
        print(f"Valor do depósito: R$ {valor}")
        print("Data do depósito: ", end="")
        Data()

    def saca(self, valor):
        self.saldo -= valor
        print(f"Valor do saque: R$ {valor}")
        print("Data do saque: ", end="")
        Data()