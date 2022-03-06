"""
Estilo de guias para as funções

PEP 8 -pROPOSTA DE MELHORIA NO PYTHON

Este documento fornece convenções de codificação para o código Python que compreende
a biblioteca padrão na distribuição principal do Python. Consulte o PEP informativo
complementar que descreve as diretrizes de estilo para o código C na implementação C
do Python .

O pep8 é uma ferramenta simples (e muito eficaz) que analisa o seu código Python
segundo as convenções de código descritas na PEP 8
"""


def ola_mundo():    #Definir uma função
    return 'Hello Mundo'

print(ola_mundo())
print(type(ola_mundo))

def ola_pessoal():
    pass

resultado = ola_pessoal()

type(resultado)


def ola(nome, idade):
    return f'Olá {nome}, você tem {idade} anos'

print(ola('Dácio', 31))
print(ola('Henrique', 29))

def ola(nome, sobrenome, idade):
    return f'Olá {nome} {sobrenome}, você tem {idade} anos'

print(ola('Dácio','Coelho', 31))
print(ola('Henrique','Machado', 29))

def ola(nome, sobrenome, idade=33):  #CrRIAÇÃO DE PARAMETRO OPCIONAL
    return f'Olá {nome} {sobrenome}, você tem {idade} anos'

print(ola('Dácio','Coelho'))


def ola(nome= 'João', idade= 19):
    return f'Olá {nome}, você tem {idade} anos'

print(ola(nome= 'Dácio'))

