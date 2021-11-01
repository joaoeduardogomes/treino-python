lanche = ('hambúrguer', 'suco', 'pizza', 'pudim') # imutáveis
print(lanche[1]) # é o suco, pois a ordem dos elementos é 0 1 2 3
print(lanche[1:3]) # Vai imprimir os elementos 1 e 2 (desconsidera o último)
print(lanche[2:]) # imprime do 2 até o final
print(lanche[:2]) # imprime do 0 ao 2 (desconsiderando o 2)
print(lanche[-1]) # imprime o pudim, porque o -1 começa do último elemento e percorre o caminho da direita pra esquerda.

"""Não é possível atribuir valores fora da tupla.
Ex: 'lanche[1] = 'refrigerante' """

for comida in lanche:
    print(f"Eu vou comer {comida}.") #Ele vai criar uma variável temporária (comida) e preencher ela com cada item da variável 'lanche', um de cada vez. Isto é, o programa vai rodar o laço 4 vezes, sendo que em cada vez 'comida' é substituído por um dos valores de 'lanche' (na ordem).
print("Comi pra caramba!") # Terminado o laço, vai imprimir esta parte.

# ou:

for cont in range(0, len(lanche)+1):
    print(lanche[cont]) #imprime o lanche na posição 'cont'

# ou:

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}.") 