"""
Crie um programa que tenha uma tupla com várias palavras (sem acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('cachorro', 'gato', 'coruja', 'tubarao', 'jabuti', 'hamster', 'coala')

for cont in palavras:
    print(f"\nNa palavra {cont.upper()} temos ", end="") #pode ser só "cont" ao invés de "palavras[cont]" porque ele já tá fazendo o 'for' dentro da tupla.
    for letra in cont:
        if letra.lower() in 'aeiou': # Aqui estabelecemos a condição. Se tiver qualquer uma das letras estabelecidas, o programa imprime. Isso funciona porque cada palavra é uma lista
            print(letra, end="")