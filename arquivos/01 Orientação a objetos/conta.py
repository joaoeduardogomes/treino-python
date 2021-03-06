from datas import Data
from random import randint

class Conta:

    #os valores abaixo foram pré-definidos apenas para acelerar o teste.
    def __init__(self, numero = randint(123, 987), titular = "João", saldo = 50.0, limite = 1000.0):
        print(f"Construindo objeto...{self}")
        #O self será o código do objeto. Ele é a referência do objeto criado.
        """
        Basta seguir o passo a passo no console:
        1) "from b_conta import Conta"
        2) conta = Conta()
        """
        #Os valores abaixo podem tanto ser especificados após o ponto como serem introduzidos pelo usuário. Para o segundo caso, basta pedir esses parâmetros no "def" e colocá-los no "self" abaixo.
        self.__numero = numero 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #O "__" impede que o parâmetro seja acessado diretamente. Dessa forma, é preciso uma função para acessar seu valor. Ex: para acessar o saldo, enquanto houver "__", só será possível pelo método "extrato()".

    def extrato(self):
        print(f"Saldo R$ {self.__saldo} do titular {self.__titular}")
        print("Data do extrato: ", end="")
        Data()

    def deposita(self, valor):
        self.__saldo += valor
        print(f"Valor do depósito: R$ {valor}")
        print("Data do depósito: ", end="")
        Data()

    def __pode_sacar(self, valor_a_sacar):
        saque_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= saque_disponivel
        #Ele devolve True se a condição do método "saca" for cumprida conforme este método

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f"Valor do saque: R$ {valor}")
            print("Data do saque: ", end="")
            Data()
        else:
            print(f"O valor R$ {valor} excede seu limite de R$ {self.__limite}")

    def transfere(self, valor, destino):
        #origem.saca(valor) -> substituído pelo self abaixo
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self): #"get_" retornam informações
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite): #"set_" enviam informações
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}