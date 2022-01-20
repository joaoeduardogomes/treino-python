'''
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

** usar outro site, pois o antivírus diz que o site não é seguro
'''

import urllib
import urllib.request

print()

try:
    site = urllib.request.urlopen('https://gamestalk.net')
except:
    print("O site não é acessável nesta máquina.")
else:
    print("O site é acessável nesta máquina!")

print()