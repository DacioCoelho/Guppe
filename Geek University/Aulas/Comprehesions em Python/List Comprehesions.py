"""
List Comprehesion

Utilizando List Comprehension nós podemos gerar listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprension

[ dado for dado in iterável ]

# Exemplos:

numeros = [1, 2, 3, 4, 5]

res = [ numero * 10 for numero in numeros]

print(res)

res = [ numero - 10 for numero in numeros]

print(res)

res = [ numero / 10 for numero in numeros]
print(numeros)
print(res)


def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)


Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda aprte: numero * 10


# List Comprehension versos Loop

# Loop

numeros =  [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])



# Outros exemplos

nome = 'Dácio Coelho'

print([alfa.upper() for alfa in nome])

# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['henrique', 'david', 'Arthur', ]

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([numero * 2 for numero in range(1,5)])

"""

"""
Aprofundando em List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

"""

# Exemplos
# 1

numeros = [1, 2, 3, 4, 5, 6]