# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a "R$1.250,00", calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Informe seu salário para saber seu aumento: "))

if salario > 1250:
    print(f"Seu salário terá um aumento de 10%, ou seja, R$ {salario * 0.1} a mais. Agora, você irá ganhar {(salario * 1.1):.2f}")
else:
    print(f"Seu salário terá um aumento de 15%, ou seja, R${salario * 0.15} a mais. Agora, você irá ganhar {(salario * 1.15):.2f}")
