class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtidas = 0

    def curtir(self):
        self._curtidas += 1

    @property
    def nome(self):
        return self._nome

    @property
    def curtidas(self):
        return self._curtidas

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def __str__(self):
        return f"""
        {self._nome}
        {self.ano}
        {self.curtidas} curtida(s)
        """


class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) 
        self.duracao = duracao

    def __str__(self):
        return (f"""
        {self._nome}
        {self.ano}
        {self.duracao} minutos
        {self.curtidas} curtida(s)
        """)

class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f"""
        {self._nome}
        {self.ano}
        {self.temporadas} temporadas
        {self.curtidas} curtida(s)
        """)


print()
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.curtir()


atlanta = Serie("atlanta", 2018, 2)
atlanta.curtir()
atlanta.curtir()


filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)