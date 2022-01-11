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
        self.__numero = numero 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #O "__" impede que o parâmetro seja acessado diretamente. Dessa forma, é preciso uma função para acessar seu valor. Ex: para acessar o saldo, enquanto houver "__", só será possível pelo método "extrato()".

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")
        print("Data do extrato: ", end="")
        Data()

    def deposita(self, valor):
        self.__saldo += valor
        print(f"Valor do depósito: R$ {valor}")
        print("Data do depósito: ", end="")
        Data()

    def saca(self, valor):
        self.__saldo -= valor
        print(f"Valor do saque: R$ {valor}")
        print("Data do saque: ", end="")
        Data()

    def transfere(self, valor, destino):
        #origem.saca(valor) -> substituído pelo self abaixo
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self): #"get_" retornam informações
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite): #"set_" enviam informações
        self.limite = limite