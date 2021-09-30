'''pessoas = {'nome': 'João', 
            'sexo': 'M', 
            'idade': 28}

print(pessoas)
print(pessoas['nome'])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) # Ele mostra 3 tuplas dentro de uma lista

#mostrando os dados por for:
for valor in pessoas.values():
    print(valor)

#mostrando chaves + seus respectivos valores: 
del pessoas['sexo'] #remove o item 'sexo'
pessoas['nome'] = 'Caio' #altera o valor do item 'nome'
pessoas['peso em Kg'] = 98.5 #adiciona o item 'peso em Kg' com o valor '98.5'
for chave, valor in pessoas.items():
    print(f"{chave} = {valor}")'''

#----------------
'''brasil = []
estado1 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
estado2 = {'uf': 'Paraná', 'sigla': 'PR'}
brasil.extend([estado1, estado2])
print(brasil)
print(brasil[1])
print(brasil[0]['uf'])'''

#-------------------
estado = {}
brasil = []

for c in range (0, 3):
    estado['uf'] = str(input("Unidade Federativa: ")).title()
    estado['sigla'] = str(input("Sigla do Estado: ")).upper()
    brasil.append(estado.copy())

for estado in brasil:
    print(estado)

for estado in brasil:
    for valor in estado.values():
        print(valor, end=" ")
    print()