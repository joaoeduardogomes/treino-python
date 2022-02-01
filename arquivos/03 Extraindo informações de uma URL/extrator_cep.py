import re # Regular Expression -- RegEx

endereco = "Rua Lasar Segall, 80, apartamento 3002, São Sebastião, Porto Alegre, RS, 91060-530"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") # estabelecendo um padrão (CEP)
# o "?" indica que o dado imediatamente anterior a ele pode aparecer nenhuma ou uma vez. Assim, ele retorna o CEP com ou sem "-"

busca = padrao.search(endereco) # retorna um obj match ou None (caso o padrão não seja encontrado)

if busca:
    cep = busca.group()
    print(cep)