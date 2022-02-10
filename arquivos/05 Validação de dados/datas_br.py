from datetime import datetime, timedelta
#o timedelta serve pra simularmos dias à frente, assim podemos fazer alguns testes como: tempo de cadastro, tempo restante para algo etc.

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        mes_cadastro = self.momento_cadastro.month - 1 #porque ele conta os meses de 1 a 12, e a lista vai de 0 a 11
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dias_da_semana =  ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro