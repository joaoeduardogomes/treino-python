# Faça um programa que leia um número INTEIRO qualquer e mostre na tela a sua tabuada

n = int(input("Digite um número inteiro: "))
multiplicador = 1

print("-" * 12)
print(f"A tabuada de {n} é:")

while (multiplicador <= 10):
    print(f"{n} x {multiplicador:2} = {n*multiplicador}")
    multiplicador = multiplicador + 1

print("-" * 12)

# o ":2" é pra que os números ocupem 2 dígitos de espaço. Assim fica tudo alinhado com o 10, que naturalmente ocupa dois dígitos.