"""
Entendendo Kwargs - duplo asterisco **kwargs (Recebeu esse nome por convenção)

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em tupla,
 o **kwargs exige que utilizamos parâmetros NOMEADOS, e transforma esses parâmetros extras em dicionário.

 # Exemplo

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(Marcos='verde', Júlia='Rosa', Pedro= 'Vermelho', Ana='Preto')

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')

cores_favoritas(Marcos='Verde', Júlia='Rosa', Pedro= 'Vermelho', Ana='Preto')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.
cores_favoritas(Marcos='Verde', Júlia='Rosa')
cores_favoritas()

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'nome' in kwargs and kwargs['nome'] == 'Dácio':
        return 'Você é muito especial, pequeno gafanhoto'
    elif 'nome' in kwargs:
        return f"{kwargs['nome']} tudo bem? Seu cadastro esta incompleto"
    return 'Não reconheço você'

print(cumprimento_especial())
print(cumprimento_especial(nome= 'Dácio'))
print(cumprimento_especial(nome= 'Oi!'))
print(cumprimento_especial(nome='Python'))

# Nas nossas funções, podemos ter (nesta ordem):

    - Parâmetros obrigatórios:
    - *args:
    - Parâmetros default (Não obrigatórios):
    - **kwargs


def minha_funcao(idade,nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Dácio')
minha_funcao(18, 'Carlos', 4,5, 3, solteiro=True)
minha_funcao(34, 'Alexandre', eu='Não', você='Vai')


# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Dácio', 'sobrenome': 'Coelho'}

print(mostra_nomes(**nomes))
"""
