from validate_docbr import CPF
from cpf_cnpj import Documento

print()

#cpf = "78965412352" # precisa ser 'str' porque 'int' não tem 'len'

#objeto_cpf = Cpf(cpf)

'''cpf = CPF()

print(cpf.validate("789.654.123-52"))'''

cpf_um = '26135229095'
documento = Documento.cria_documento(cpf_um)
print(f"CPF: {documento}")

cnpj_um = '82660142000140'
documento2 = Documento.cria_documento(cnpj_um)
print(f"CNPJ: {documento2}")

print()