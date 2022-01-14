"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(largura, comprimento):
    print('-' * 20)
    print(f"O terreno informado tem largura de {largura}m e comprimento de {comprimento}m. Portanto, sua área total é de {largura * comprimento}m².")
    print('-' * 20)


largura = float(input("Informe a largura do terreno em metros: "))
comprimento = float(input("Informe o comprimento do terreno em metros: "))

area(largura, comprimento)