from abc import ABC
# abc = abstract base classes

from collections.abc import MutableSequence
from numbers import Complex

class Playlist(MutableSequence):
    pass

class Numero(Complex):
    pass

filmes = Playlist()
num = Numero()
# Ao tentar printar, ele vai dizer todos os métodos que devem ser implementados para o print funcionar.