"""
Crie um programa em que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão matemática passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = str(input("Digite sua expressão matemática. Atenção aos parênteses. "))
pilha = []
for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0: #se a pilha não estiver vazia
            pilha.pop() # remove o último elemento de uma lista.
        else: #se a pilha estiver vazia
            pilha.append(")")
            break
'''A lógica desse "for" é que ele testa se tem "(" na pilha. Cada "(" identificado é adicionado à pilha e cada ")" exclui um "(" da pilha. É como se ele encontrasse seu par e os dois sumissem. Se o programa identificar a entrada de um ")" mas a pilha estiver vazia, ele vai dar erro.'''

if len(pilha) == 0:
    print("A espressão inserida é válida!")
else:
    print("A expressão inserida é inválida.")




#ou, sem usar listas podemos fazer: 
"""expressao = str(input('Digite sua expressão matemática. Atenção aos parênteses. '))

if expressao.count('(') == expressao.count(')'):

    print('A espressão inserida é válida!')

else:

    print('A expressão inserida é inválida...')"""