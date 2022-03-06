"""
Módulo Collections - Default Dict # Melhorias para alta performace

https://docs.python.org/3/library/collections.html#collections.defaultdict

Dict - Dicionários

dicionario = {'Curso': 'A Beira da Quadra'}

print(dicionario)
print(type(dicionario))

print(dicionario['Curso'])

# print(dicionario['Esqueci']) # Gera um erro KeyError

# Para evitar o KeyError, é utilizado o Default Dict

Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda
para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe,
essa chave será criada e o valor default será atribuido

OBS: Lambdas são funcções sem nome, que podem ou não receber parâmetros de retornar valores.
"""

# Fazendo import

from collections import defaultdict

dicionário = defaultdict(lambda: 0)

print(dicionário)

dicionário['curso'] = 'A Beira da Quadra'

print(dicionário)

print(dicionário['outro']) # KeyError no dicionário comum, mas aqui não

print(dicionário)


