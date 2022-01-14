primeiroNumero = int(input ("Digite o primeiro número: "))
segundoNumero = int(input ("Digite o segundo número: "))
# É importante colocar o valor dentro do "int()" para que seja interpretado como um número, não como uma string.

soma = primeiroNumero + segundoNumero

#print("A soma dos dois números é:{}".format(soma))
# O modo acima é mais antigo. O mais moderno é o abaixo.

print(f"A soma dos valores {primeiroNumero} + {segundoNumero} é: {soma}")
