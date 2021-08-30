# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja, errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo (M/F): ")).strip().lower()

while (sexo != 'm' and sexo != 'f') and (sexo != 'masculino' and sexo != 'feminino'):
    sexo = str(input("Opção inválida. Tente novamente (M/F): ")).strip().lower()

if sexo == 'f' or sexo == 'feminino':
    print(f"Sexo: feminino.")
elif sexo =='m' or sexo == 'masculino':
    print("Sexo: masculino.")
print("Fim do programa.")