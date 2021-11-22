"""
Crie um programa que tenha a função 'leiaInt()', que vai funcionar de forma semelhante á função 'input()' do Python, mas que fará a validação para aceitar apenas um valor numérico.
* Ele deve mostrar o número digitado
* Se não for número inteiro, ele dá erro e continua perguntando

ex:
n = leiaInt('Digite um número: ')
"""

def leiaInt():
    while True:
        try:
            print('~~' * 20)
            n = int(input("Digite um número inteiro: "))
            print('~~' * 20)
            break
        except ValueError:
            print(f"Erro! O valor inserido não é um número inteiro.")
            continue

    print(f"O número inteiro que você digitou foi: {n}")

leiaInt()