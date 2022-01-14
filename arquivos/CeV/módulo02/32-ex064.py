"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag, que é a condição de parada)
"""
numeros = []
num = 0

while num != 999:
    num = int(input(f"Digite um número inteiro qualquer. Ou digite 999 para encerrar o programa. \n>>>Sua entrada: "))
    if num != 999:
        numeros.append(num)
    print("-="*10)

print(f"Os números digitados foram: {numeros}")
print(f"A quantidade de entradas foi: {len(numeros)}")
print(f"A soma total entre eles é: {sum(numeros)}")