"""
Crie um programa em que o usuário possa digitar cinco valores numéricos e cadastrá-los em uma lista.
No final, mostre a lista ordenada na tela sem usar o sort().
"""

numeros = []

maior = 0
menor = 0
for cont in range (1, 6):
    num = int(input(f"Digite um número inteiro para inseri-lo à lista {cont}/5: "))
    if cont == 1 or num > numeros[-1]: # Ou " > numeros[len(numeros)-1". A ideia é pegar o último número da lista.
        numeros.append(num)
        print(f"Adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(numeros): #ele testa em cada posição da lista se o número inserido é menor do que o registrado na respectiva posição verificada.
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos += 1
print("=-"*20)
print(f"Lista em ordem crescente dos valores digitados: {numeros}")