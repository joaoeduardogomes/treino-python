# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número inteiro: "))
nDobro = n * 2
nTriplo = n * 3
nRaiz = n ** (1/2)

print(f"O dobro de {n} é {nDobro}. \nSeu triplo é {nTriplo}. \nE sua raiz quadrada é {nRaiz:.2f}.")
