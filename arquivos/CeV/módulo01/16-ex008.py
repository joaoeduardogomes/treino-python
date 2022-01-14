# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
#acrescentar Km, hm, dam, dm

n_m = float(input("Digite um valor em metros: "))
n_km = n_m * 0.001
n_hm = n_m * 0.01
n_dam = n_m * 0.1
n_dm = n_m * 10
n_cm = n_m * 100
n_mm = n_m * 1000

print("{n_m}m equivale a:")
print(f"{n_km}Km \n{n_hm}hm \n{n_dam}dam \n{n_dm}dm \n{n_cm}cm \n{n_mm}mm")
