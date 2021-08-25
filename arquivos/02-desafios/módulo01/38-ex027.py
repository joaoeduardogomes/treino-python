# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input("Informe seu nome completo: ")).title().strip()
n = nome.split()

print(f"Verificamos que seu primeiro nome é {n[0]}")
print(f"Verificamos que seu último nome é {n[len(n)-1]}")
#Sem o -1 ele dá erro porque vai uma posição além, e não tem nada lá.
