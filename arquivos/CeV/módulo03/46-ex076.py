"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

produtos = ('PlayStation 5', 4699.90, 
            'DualSense', 449.90, 
            'Headset', 429.90, 
            'God of War', 39.90, 
            'Persona 5', 39.90, 
            'The Last of Us', 199.90, 
            'Spider-Man', 119.90)
print('~~'*20)
print(f"{'A lista de preços é:':^40}")
print('~~'*20)
for cont in range (0, len(produtos)): #com "...", alinhado à esquerda e ocupando 30 espaços.
    if cont % 2 == 0:
        print(f"{produtos[cont]:.<30}", end="") 
    else:
        print(f"R$ {produtos[cont]:>7.2f}")
print('-='*20)