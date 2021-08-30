"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
"""

print("Informe dois valores e selecione a operação que desja fazer com eles.")
valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

opcao = int(input("""O que deseja fazer com esses números?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] saber qual é maior
[ 4 ] informar novos números
[ 5 ] sair do programa
Sua escolha: """))

while opcao != 5:
    if opcao == 1:
        print(f"A soma de {valor1} + {valor2} é: {valor1 + valor2}.")
    elif opcao == 2:
        print(f"A multiplicação de {valor1} com {valor2} é {valor1 * valor2}.")
    elif opcao == 3:
        if valor1 > valor2:
            print(f"O maior valor é {valor1}.")
        elif valor2 > valor1:
            print(f"O maior valor é {valor2}.")
        else:
            print(f"{valor1} e {valor2} são iguais.")
    elif opcao > 5 or opcao < 1:
        print("Opção inválida. Tente novamente.")

    valor1 = int(input("Informe o primeiro valor: ")) #Aqui já funciona como opção 4
    valor2 = int(input("Informe o segundo valor: "))

    opcao = int(input("""O que deseja fazer com esses números?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] saber qual é maior
    [ 4 ] informar novos números
    [ 5 ] sair do programa
    Sua escolha: """))
print("Fim do programa.")