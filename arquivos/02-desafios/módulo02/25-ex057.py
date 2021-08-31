# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja, errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo (M/F): ")).strip().lower()[0] #Com esse "0" o programa só pega a primeira letra, então é possível usar só 'm' e 'f' na validação.

while sexo not in 'mf':
    sexo = str(input("Opção inválida. Tente novamente (M/F): ")).strip().lower()[0]

if sexo == 'f':
    print(f"Sexo registrado: feminino.")
elif sexo =='m':
    print("Sexo registrado: masculino.")
print("Fim do programa.")