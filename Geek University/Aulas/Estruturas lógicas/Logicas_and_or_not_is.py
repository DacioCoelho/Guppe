"""
Estruturas lógicas  = And, or, not e is

and = e
or = ou
not = não
is = é

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o "and", ambos os valores precisam ser True
Para o "or", um ou outro precisa ser True
Para o "not", o valor do booleano é invertido
Para o "is", o valor é comparado com um segundo(comparação)
"""

ativo = False
logado = False

if ativo is False:
    print('Você precisa ativar sua conta')
else:
    print('Bem-vindo usuário')

