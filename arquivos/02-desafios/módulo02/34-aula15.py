# Uma boa maneira de usar o break:

num = soma = 0 # Aqui só declaramos que ambas as variáveis iniciam com o valor 0

while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    soma += num #Aqui ele não vai considerar o '999' na soma, porque o loop é quebrado antes
print(f"A soma vale {soma}")