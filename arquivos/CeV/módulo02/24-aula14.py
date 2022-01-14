""""
for contador in range(1, 10):
    print(contador)
print('fim')

ou

contador = 1
while contador < 10:
    print(contador)
    contador += 1
print("Fim")   """

while n != 0:   #Esta estrutura não funciona no for, porque não delimita final antes.
    n = int(input("Digite um valor: "))
print("Fim.")