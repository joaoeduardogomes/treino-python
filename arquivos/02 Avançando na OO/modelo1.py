class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)

print()
print(f"""
Nome: {vingadores.nome}
Ano: {vingadores.ano}
Duração: {vingadores.duracao}min
""")
print('\n')

atlanta = serie("Atlanta", 2018, 2)
print(f"Nome: {atlanta.nome} \nAno: {atlanta.ano} \nTemporadas: {atlanta.temporadas}")





print()