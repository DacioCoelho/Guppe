"""
Parâmetros variavéis
"""
def soma(*args):
    aux = 0
    for valor in args:
        aux += valor
        return aux

print(soma())
print(soma(2, 4, 6))

def f(**kwargs):
    print(kwargs)
    print(type(kwargs))

print(f(nome = 'Dácio', sobrenome = 'Coelho'))

args = (2, 4, 10)
kwargs = {'nome': 'Dácio', 'sobrenome': 'Coelho'}

def f(*args, **kwargs):
    print(args)      # Tupla
    print(kwargs)    # Dicionário

print(f())
print(f(1,2,nome = 'Dácio', sobrenome = 'Coelho' ))