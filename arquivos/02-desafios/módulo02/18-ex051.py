# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo1 = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Informe a razão da PA: "))
termo = termo1

print("Os dez primeiros termos da PA são:")
for contador in range (1, 11):
    termo = termo + razao
    print(f"{termo}")
