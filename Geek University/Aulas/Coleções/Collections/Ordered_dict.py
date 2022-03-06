""""
Módulo Collections - Ordered Dict


# Em um dicionário a ordem de inserção dos elementos não é garantida

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd':4}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'Chave = {chave} e valor = {valor}')

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd':4})

print(dicionario)
print(type(dicionario))

for chave, valor in dicionario.items():
    print(f'Chave = {chave} e Valor = {valor}')

# COM A ORDERED DICT NÓS TEMOS A CERTEZA QUE O DICIONÁRIO TERÁ A ORDEM DE INSERÇÃO DOS ELEMENTOS

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comun
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'b': 1}

print(dict1 == dict2) # True -> A ordem dos elementos não importa para o dicionário.

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'a': 2, 'b': 1})

print(odict2 == odict1)

"""
from collections import OrderedDict

