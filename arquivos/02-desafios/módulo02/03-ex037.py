# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
"""
1 para binário
2 para octal
3 para hexadecimal
"""

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
    # o [2:] é para começar a martir do 3º item (0, 1, 2) e ir até o final da string. Isso para cortar informações de conversão como b0, 0c e hex — que aparecem antes od número convertido.
elif opcao == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválida. Tente novamente.")
