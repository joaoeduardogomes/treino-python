# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date

ano = int(input("Informe um ano para saber se ele é bissexto. Se quiser analisar o ano atual, digite 0(zero). "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
