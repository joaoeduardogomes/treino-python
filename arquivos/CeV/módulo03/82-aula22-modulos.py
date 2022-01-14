# Trabalhando com módulos

import uteis
"""
Neste caso, "uteis" é o nome do módulo
No caso de fazer "from uteis import fatorial", o "úteis" seria o módulo e o "fatorial seria a função desse módulo
"""

print()
num = int(input("Digite um valor para ver seu fatorial: "))
fat = uteis.fatorial(num)

print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {uteis.dobro(num)}")
print(f"O triplo de {num} é {uteis.triplo(num)}")