# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

str(input("Que tal se eu lhe mostrar todos os números pares no intervalo de 1 a 50? Pressione ENTER se estiver preparado."))

for num in range (2, 51, 2):
    print(num, end=", ")
