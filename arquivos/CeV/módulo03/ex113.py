'''
**Referente à aula 23 — tratamento de erros:

Reescreva a função "leiaInt()", que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função "leiaFloat()" com a mesma funcionalidade.
'''

def leiaInt():
    while True:
        try:
            print('~~' * 20)
            n = int(input("Digite um número inteiro: "))
            print('~~' * 20)
            break
        except ValueError:
            print(f"ERRO! O valor inserido não é um número inteiro.")
            continue

    print(f"O número inteiro que você digitou foi: {n}")

def leiaFloat():
    while True:
        try:
            print('--' * 20)
            n = float(input("Digite um número real: "))
            print('--' * 20)
            break
        except ValueError:
            print("Erro! o número que você digitou é inválido")
            continue
    print(f"O número que você digitou foi: {n}")

leiaInt()
leiaFloat()