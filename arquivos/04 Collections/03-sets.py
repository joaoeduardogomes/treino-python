print()

time1 = ['tsuna', 'yamamoto', 'hayato']
time2 = ['mukuro', 'hibari', 'yamamoto']

conjunto = set(time1 + time2)

print(conjunto)

print('-' * 30)
equipe1 = set(time1)
equipe2 = set(time2)

print(f"{equipe1 & equipe2} está nas duas equipes.")
print(f"{equipe1 - equipe2} estão só na equipe 1.")
# mostra os membros de um set, excluindo os que se repetem no outro.
print(f"{equipe2 - equipe1} estão só na equipe 2.")



print()