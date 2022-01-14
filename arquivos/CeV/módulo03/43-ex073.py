"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre: (usei 15 times da confederação oeste da NBA)
A) apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense. (usei o time L.A. Lakers)
"""

times = ('Mavericks', 'Nuggets', 'Rockets', 'Clippers', 'Lakers', 'Grizzlies', 'Timberwolves', 'Pelicans', 'Suns', 'Blazers', 'Kings', 'Spurs', 'Jazz', 'Warriors', 'Thunder')

print('~~'*30)
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print('~~'*30)
#print(f"Os últimos 4 colocados são: {times[14:10:-1]}") #Assim mostra do Thunder pra trás
print(f"Os últimos 4 colocados são: {times[11:]}") #ou 'times[-4:]'
print('~~'*30)
print(f"A lista com todos os times em ordem alfabética é: {sorted(times)}")
print('~~'*30)
print(f"O time Los Angeles Lakers aparece na {times.index('Lakers')+1}ª posição.")
print('~~'*30)