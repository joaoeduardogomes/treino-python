nome = input("Informe seu nome: ")
#print ("Prazer em te conhecer, {:20}!".format(nome))
#No exemplo acima, ele vai escrever o nome num espaço de 20 caracteres
# Vai ficar: "Prazer em te conhecer, antonio             !"

#print ("Prazer em te conhecer, {:>20}!".format(nome))
#Acima, com ">", vai alinhar o nome à direita
# Vai ficar: "Prazer em te conhecer,                 João!"

#print ("Prazer em te conhecer, {:<20}!".format(nome))
#Com "<", vai alinhar à esquerda

#print ("Prazer em te conhecer, {:^20}!".format(nome))
#Com "^", vai alinhar ao centro

#print ("Prazer em te conhecer, {:=^20}!".format(nome))
# No modelo acima, vai alinhar ao centro e imprimir "=" nos espaços vazios
# Vai ficar: "Prazer em te conhecer, ========João========!"

# MODELO MAIS NOVO:
print(f'Prazer em te conhecer, {nome:=^20}!'.upper())