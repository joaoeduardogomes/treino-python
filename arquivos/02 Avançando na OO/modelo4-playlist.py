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


class Filme (Programa): #A classe mãe é passada entre parênteses
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #Não precisa passar o "self", pois ele sabe que os param. vêm da superclasse "Programa"
        #Ele chama o inicializador da classe-mãe
        self.duracao = duracao


class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


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

print('-'*20)

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas

    print(f"""
    {programa.nome}
    {detalhes}
    {programa.curtidas}
    """)