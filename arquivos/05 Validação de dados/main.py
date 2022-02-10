from validate_docbr import CPF
from cpf_cnpj import Documento
import re
from TelefonesBr import TelefonesBr
from datetime import datetime, timedelta
from datas_br import DatasBr

print()

#cpf = "78965412352" # precisa ser 'str' porque 'int' não tem 'len'

#objeto_cpf = Cpf(cpf)

'''cpf = CPF()

print(cpf.validate("789.654.123-52"))'''


# CPF + CNPJ:
'''cpf_um = '26135229095'
documento = Documento.cria_documento(cpf_um)
print(f"CPF: {documento}")

cnpj_um = '82660142000140'
documento2 = Documento.cria_documento(cnpj_um)
print(f"CNPJ: {documento2}")'''

# Telefone: 
'''padrao = "[0-9][a-z][0-9]" #o padão é: num + letra + num
texto = "123 1a2 1cc aal" #'1a2' é num + letra + num
resposta = re.search(padrao, texto) #procura um padrão dentro de um texto

print(resposta.group())'''

'''padrao_molde = '(zz)aaaa-wwww'
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "Eu gosto do número: 54981118826 e gosto também do número 48994556785"
resposta = re.findall(padrao, texto)'''

'''telefone = "05554981118826"
telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto)'''

# Datas: 
'''hoje = DatasBr()
print(hoje.tempo_cadastro())'''



print() 