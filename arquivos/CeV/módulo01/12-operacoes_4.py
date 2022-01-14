n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
exponenciacao = n1 ** n2

print(f"A soma é {soma}, \n a subtracao é {subtracao} \n e a multiplicacao é {multiplicacao}.", end="")
print(f" A divisão é {divisao}, a divisão inteira é {divisaoInteira} e a exponenciação é {exponenciacao}.")

#Alternativa:
# print(f" A divisão é {divisao:.3f}.")
# Dessa forma, quando o número depois da vírgula for muito grande, o valor vai aparecer em 3 casas decimais aceitando números flutuantes (f).