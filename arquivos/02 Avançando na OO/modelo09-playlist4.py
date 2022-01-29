#duck typing

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
        {self.temporadas} temporada(s)
        {self.curtidas} curtida(s)
        """)

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__ (self, item):
        return self._programas[item]
        # permite iterar or itens da lista

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


print()
belezaamericana = Filme("beleza americana", 1999, 122)
cobrakai = Serie("cobra kai", 2018, 4)
panico = Filme("pânico", 1996, 111)
invincible = Serie("invincible", 2021, 1)

belezaamericana.curtir()
belezaamericana.curtir()
cobrakai.curtir()
cobrakai.curtir()
cobrakai.curtir()
cobrakai.curtir()
panico.curtir()
panico.curtir()
panico.curtir()
invincible.curtir()

filmes_e_series = [belezaamericana, cobrakai, panico, invincible]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


print(f"Tamanho da playlist: {len(playlist_fim_de_semana)} títulos")

for programa in playlist_fim_de_semana:
    print(programa)

print(f" Tá ou não tá? {cobrakai in playlist_fim_de_semana}") #verifica se um título tá numa playlist

print(playlist_fim_de_semana[1]) #título na posição 1