# LISTAS

num = [2, 5, 9, 1]
num[2] = 3 # o 9 passa a valer 3. Esse tipo de atribuição não é possível na tupla. Mas não é possível usar essa atribuição pra adicionar novos valores e expandir a lista. Para tanto, é preciso fazer "num.append(valor)"
num.append(7) # Adiciona o 7 à lista.
num.sort(reverse=True) # mostra a lista em ordem invertida (decrescente)
num.insert(2, 0) # Adiciona o número 0 na posição 2, reorganizando os demais.
num.pop(2) # Elimina o valor na posição 2, que atualmente é o 0
print(num)

#--------------
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f"{v}...", end="") # Ele vai imprimir "5...9...4..."
print(f"\n")

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!") #aqui ele diz em qual posição ele encontrou o valor.
print("Cheguei ao final da lista.")

#-------
valores = []

for cont in range (0, 5):
    valores.append(int(input("Digite um valore: "))) # Maneira mais eficar de guardar um número sinerido pelo teclado.
print(valores)

#------------
a = [2, 3, 4, 7]
b = a
b[2] = 8 #Ao fazer isso, o Python muda o 4 por 8 em ambas as listas. Porque não criamos cópia de uma em outra, mas sim as igualamos ao fazer "b = a". Ao fazer isso, o Python cria uma ligação entre elas, e cada alteração em uma é aplicada em ambas.
b = a[:] # Desta maneira fazemos o "b" receber todos os valores de "a". Assim fazemos uma cópia de fato.