# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².

# 1L - 2m²
# xL - Altura x Largura (m²)

altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))
area = altura * largura

print(f"Para pintar uma área de {area}m², você vai precisar de {area / 2}L de tinta")