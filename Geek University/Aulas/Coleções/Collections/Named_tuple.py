"""
Módulo Collections - Named tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recapitulação de Tupla

tupla = (1, 2, 3)

print(tupla[1])

# Named Tuple -> Tupla Nomeada
                São tuplas diferenciadas ondes, especificamos um nome para a mesma e também parâmetros.
"""

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro','idade, raça, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='Golden Retriver', nome='Ray')
rapa = cachorro(idade=3, raça='Golden Retriver', nome='Rapa')
naruto = cachorro(idade=5, raça='Poddle', nome='Naritin')

print(ray)
print(rapa)
print(naruto)

# Acessando os dados (Muito mais intuitivo

# FORMA 1
print(rapa[0])
print(rapa[1])
print(rapa[2])

# FORMA 2
print(rapa.idade)
print(rapa.raça)
print(rapa.nome)

print(ray.index('Golden Retriver'))

print(ray.count('Golden Retriver'))