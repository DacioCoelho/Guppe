"""
Entendendo *args

- Parâmetro especial, ele é como qualquer outro. Isso significa que você poderá chamar
 de qualquer coisa, desde que comece com asterisco.

 O parâmetro *args em uma função, coloca os valores extras informados como
 entrando em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplo 1

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 5 ,8))

# print(soma_todos_numeros(4, 5)) - TypyError

#print(soma_todos_numeros(4, 5, 8, 9)) - TypyError

def soma_todos_numeros(num1=1, num2=2, num3=1):  # SEM TypyError
    return num1 + num2 + num3

print(soma_todos_numeros(4, 5 ,8))

print(soma_todos_numeros(4, 5))

# print(soma_todos_numeros(4, 5, 8, 9)) - TypyError


# Entendendo o *args

def soma_tudo(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

soma_tudo()
soma_tudo(1)
soma_tudo(1, 2)
soma_tudo(1, 2, 3)

print(soma_tudo())
print(soma_tudo(1))
print(soma_tudo(1, 2))
print(soma_tudo(1, 2, 3))

def soma_tudo(*args):
    return sum(args)

print(soma_tudo())
print(soma_tudo(1))
print(soma_tudo(1, 2))
print(soma_tudo(1, 2, 3))

# FUNÇÃO recebendo o *args nós podemos passar a quantidade de
# parametros que desejarmos, que ela vai corresponder

#OBS: Lembrando que o valor tem que ser inteiro ou real


def verificando_info(*args):
    if "Geek" in args and "University" in args:
        return 'Bem Vindo Geek!'
    return 'Eu não te conheço, quem é você?'

print(verificando_info())
print(verificando_info(1, True, "Geek", 5, "University"))
print(verificando_info(1, 5 , 8, "Geek"))

# *args = é uma tupla, lembrando disso é possivel fazer tudo que se faz com a tupla em *args
"""

def soma_tudo(*args):
    return sum(args)

# Desempacotamento em Python

numeros = [1, 3, 5, 7, 9]

print(soma_tudo(*numeros))

# obs: o ASTERISCO SERVE PARA QUE INFORMEMOS PARA O PYTHON QUE ESTAMOS PASSANDO COMO ARGUMENTO
# UMA COLEÇÃO DE DADOS. DESTA FORMA, ELE SABERÁ QUE PRECISARÁ ANTES DESEMPACOTAR ESTES DADOS.