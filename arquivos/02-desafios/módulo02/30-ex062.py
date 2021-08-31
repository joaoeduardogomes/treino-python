"""
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""

termo1 = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
termo = termo1
contador = 1
total = 0
mais = 10

print("A PA é:")
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo} ➝  ", end = "")
        termo = termo + razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print("FIM DO PROGRAMA")
print(f"Progressão finalizada com {total} termos mostrados.")