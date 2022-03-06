"""
Funções com retorno

print('Python!')

numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retorno de ret = {ret}') # Função com retorno
print(numeros)

ret_pr = print(numeros)

print(f'Retorno de print = {ret_pr}') # Função sem retorno

OBS: Em Python quando uma função não retorna nenhum valor, o retorno é None (Nada)

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra
reservada: return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar
a execução da função para outras funções (Ou mesmo para o print)


# Exemplo 1

def quadrado_de_7():   #Imprimir é diferente de retornar
    print(7 * 7)

ret = quadrado_de_7()

# print(f'Retorno de ret {ret}') # O print não retorna nada

# EXEMPLO 2
# Vamos refaturar essa função. (Reescrever ou redefinir)

def quadrado_de_7():
    return 7 * 7

quadrado_de_7()

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno de ret = {ret}')
print(f'Retorno de ret = {quadrado_de_7()}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi! ' # Colocando o return me da mais flexibilidade para que eu possa utilizar o dado da função

print(diz_oi())

alguem = 'Dácio'

print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos ter, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores:

    # Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    print('Estou sendo executada antes do return...')
    return 'Oi!'
    print('Estou sendo executado após o retorno') # A linha depois do return NUNCA SERÁ EXECUTADA

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3
    return 'b'

print(nova_funcao())


# Exemplo 3 -  Podemos ter, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores:

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num2)
print(num4)
print(outra_funcao())
print(type(outra_funcao()))


# Criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
print(joga_moeda())
print(joga_moeda())
print(joga_moeda())

from random import random

def pedra_papel_tesoura():
    if random() > 0.3:
        return 'Pedra'
    elif random() > 0.6:
        return 'Tesoura'
    return 'Papel'

print(pedra_papel_tesoura())
print(random())
print(pedra_papel_tesoura())
print(random())
print(pedra_papel_tesoura())
print(random())


# Erros comuns na utilização do retorno, que não é erro, mas sim codificação desnecessária

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    else:                # Não necessita colocar o else, pode só colcoar o return
        return False

print(eh_impar())

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
"""


