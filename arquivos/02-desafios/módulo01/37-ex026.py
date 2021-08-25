# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece na primeira vez
# Em que posição ela aparece na última vez.

frase = str(input("Digite uma frase qualquer: ")).lower().strip() #dá pra usar junto

print(f"A Letra 'a' aparece {frase.count('a')} vezes.")
print(f"A letra 'a' aparece pela primeira vez na posição {frase.find('a')+1}")
# somamos +1 para ficar de acordo com o que vemos, pois o python começa do 0.
print(f"A letra 'a' aparece pela última vez na posição {frase.rfind('a')+1}")