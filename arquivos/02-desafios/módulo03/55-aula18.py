# Listas compostas
# dados = list()  => também cria uma lista

"""dados = ('pedro', 25)
pessoas = list()
pessoas.append(dados[:]) #Assim o append insere na lista uma cópia da tupla 'dados'
#Fazendo isso, o conteúdo da tupla passa a ocupar o espaço 0 da lista. Ou seja, o espaço 0 tem  "'pedro', 25".
#A lista, supondo que foram feitas mais entradas, ficaria assim:
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) #Aqui ele vai imprimir 'Pedro', porque ele quer o elemento 0 dentro do elemento 0 maior da lista."""

#-----------------------
"""teste = list()
teste.append('João')
teste.append(28)
galera = list()
galera.append(teste[:]) #É importante colocar os [:] para criar uma cópia da lista 'teste' na lista 'galera'. Do contrário, toda alteração nos dados de 'teste' alteram os dados de 'galera'.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)"""

# Podemos fazer o exemplo acima de maneira diferente usando:
"""galera = [['João', 28], ['Ana', 33], ['Joaquim', 22], ['Maria', 45]]
for p in galera: 
    print(p) #Para cada pessoa(p) em 'galera', ele vai printar os dados.
print()
for p in galera: 
    print(f"{p[0]} tem {p[1]} anos de idade.")"""

#---------------
galera = []
dado = []
total_menor = total_maior = 0 #Essa igualdade não funciona com dados compostos, como listas
for c in range (0, 3): #Parte da inserção de dados
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:]) #Aqui ele vai adicionando a 'galera' uma cópia das informações inseridas a 'dado'.
    dado.clear() #tem que limpar os dados da entrada atual para que não seja somado à proxima

print(galera)
print()
for p in galera: #Parte da testagem
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        total_maior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        total_menor += 1

print(f"Temos {total_maior} maior(es) e {total_menor} menor(es) de idade")