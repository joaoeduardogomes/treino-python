class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtidas = 0
        #No python, não é obrigatório privar tudo. Podemos privar apenas o necessário

    def curtir(self):
        self.__curtidas += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def curtidas(self):
        return self.__curtidas

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__curtidas = 0

    def curtir(self):
        self.__curtidas += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def curtidas(self):
        return self.__curtidas

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme("vingadores - guerra infinita", 2018, 160)

print()
vingadores.curtir()
print(f"""
Nome: {vingadores.nome}
Ano: {vingadores.ano}
Duração: {vingadores.duracao}min
Curtidas: {vingadores.curtidas}
""")


atlanta = Serie("atlanta", 2018, 2)

atlanta.curtir()
atlanta.curtir()

print(f"""
Nome: {atlanta.nome} 
Ano: {atlanta.ano} 
Temporadas: {atlanta.temporadas}
Curtidas: {atlanta.curtidas}
""")
