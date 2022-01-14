# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input("Informe o salário do funcionário: R$ "))
novoSalario = salario * 1.15
# ou: salario + (salario * 15 / 100)

print(f"O salário do funcionário, com 15% de aumento, fica R$ {novoSalario:.2f}")
