# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher. Só que, agora, utilizando um laço "for".

num = int(input("Quer saber a tabuada completa de um número. Informe-o aqui: "))

for contador in range (1, 11):
    print(f"{num} x {contador:<2} = {num * contador:<2}")
