nome = str(input("QUal é o seu nome? ")).strip().title()

if nome == 'João':
    print("Temos o mesmo nome!")
elif nome == "Pedro" or nome == "Maria":
    print("Seu nome é bem popular no Brasil.")
elif nome in 'Ana Vitória Beatriz Cecília': #Aqui, qualquer uma dessas opções cumpre a condição. Ele verifica se a string se encaixa naquelas opções.
    print("Belo nome")
else:
    print("Seu nome é bem normal.")

print(f"Tenha um bom dia, {nome}")