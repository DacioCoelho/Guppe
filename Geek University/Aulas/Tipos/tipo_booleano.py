"""
Tipo Booleano

Álgebra Booleano, criado por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

# Errado:

true, false

# Certo

True, False
"""

ativo = False

print(ativo)

"""
Operações Básicas
"""

# Negação (not)
"""
Fazer a negação, se o vlor booleano for verdadeiro, o resultado será falso
se for falso, o resultado será verdadeiro. Ou seja, sempre o contrário
"""

print(not ativo)

logado = True

# Ou (or)
"""
É uma operação binária, ou seja depende de dois valores. Ou um ou o outro devem ser verdadeiro.
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
"""

print(ativo or logado)

# E (and)
"""
Operação binária, depende de dois valores.
Ambos os valores devem ser verdadeiros
True and True -> True
False and False - False
True and False -> True

>>> type(False)
<class 'bool'>
>>> type(True)
<class 'bool'>
"""

