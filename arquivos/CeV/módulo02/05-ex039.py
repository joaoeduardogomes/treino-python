""""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deve mostrar o tempo que falta ou que passou do prazo
"""

from datetime import date

ano_atual = date.today().year
print("Quer saber como está a sua idade em relação ao alistamento militar?")
sexo = str(input("Informe seu sexo (M / F): ")).strip().lower()

if sexo == "f" or sexo == "feminino":
    print("Mulheres não são obrigadas a realizar o alistamento militar.")

elif sexo == "m" or sexo == "masculino":
    ano_nascimento = int(input("Informe seu ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade == 18:
        print(f"Você deve se alistar este ano!")
    elif idade < 18:
        print(f"Você tem {idade} anos. Ainda falta(m) {18 - idade} ano(s) para o seu alistamento militar.")
        print(f"Você deve se alistar no ano {ano_atual + (18 - idade)}.")
    elif idade > 18:
        print(f"Você tem {idade} anos. Já faz {idade - 18} ano(s) desde o seu alistamento militar.")
        print(f"O ano do seu alistamento deve ter sido {ano_atual - (idade - 18)}.")

else:
    print("Opção não encontrada. Tente novamente.")
