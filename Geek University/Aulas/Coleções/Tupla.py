"""
Tuplas (tuple)

Existem básicamente duas diferenças entre tuplas e listas

 1 - As tuplas são representadas por parenteses ()
 print(type(()))

 2 - As tuplas são imutáveis, ao se criar uma tupla, ela não muda. Toda alteração em uma tupla,
  gera uma nova tupla

>>Listas são mutáveis:
lista.sort()
print(lista)
[1, 2, 3, 4, 5, 8]
lista.append(6)
lista.append(7)
print(lista)
[1, 2, 3, 4, 5, 8, 6, 7]
 lista.sort()
print(lista)
[1, 2, 3, 4, 5, 6, 7, 8]

# Cuidado 1: As tuplas são representadas por ( ), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = 4 # Sem o parenteses e virgula, o elemento sozinho não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4, # Isso é uma tupla, necessita da vírgula
print(tupla5)
print(type(tupla5))

# CONCLUSÃO -> Podemos concluir que tuplas são definidas pela virgula e não pelo uso do parênteses

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range ( inicio,fim, passo)
tupla6 = tuple(range(11))
print(tupla6)
print(type(tupla6))

# Desempacotamento de tupla

tupla = ('Dácio', 'de Oliveira Rodrigues', 'Coelho')
nome, nome_do_meio, sobrenome = tupla

print(nome)
print(nome_do_meio)
print(sobrenome)

# OBS: Gera erro (ValeuError) se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas são inexistentes, dado o fato das tuplas serem imutáveis.

# Soma*, Valor máximo*, Valor mínimo* e Tamanho
    # Se os valroes forem todos inteiros ou reais:

tupla = 1, 2, 3, 4, 5, 6
print(tupla)
print(type(tupla))
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de tuplas - juntar tuplas
tupla1 = 1, 2,3
tupla2 = 4, 5, 6
print(tupla1)
print(tupla2)

print(tupla2 + tupla1) # Tuplas são imutáveis, não somam uma a outra
print(tupla2)

tupla1 = tupla1 + tupla2 # tuplas são imutáveis, mas podemos sobreescrever seus valores
print(tupla1)


# Verificar se determinado elemento está contido na tupla

tupla = tuple(range(100))
print(tupla)

print(45 in tupla)
print(145 in tupla)


# Iterando sobre tupla
tupla = range(100)
tupla = tuple(range(5,100, 5))
print(tupla)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
    #  Contando elementos dentro de uma tupla:

tupla = ('a', 'b','c', 'a', 'd', 'b','a', 'a')
print(tupla.count('a'))
print(tupla.count('b'))
print(tupla.count('d'))

nome = tuple('Dácio de Oliveira Rodrigues Coelho')
print(nome)

print(nome.count('o'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos mudar os dados contindos em uma coleção

#Exemplo 1

meses = ('Jan','Fev','Mar','Abr','Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
print(type(meses))

meses1 = ['Jan','Fev','Mar','Abr','Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# Não faz sentido  modificar uma lista, de algo imutável, por isso ideal fazer tupla
print(type(meses1))

# O acesso a elementos de uma tupla também é semelhante a uma lista
print((meses[7]))

# Interar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i +1

# Verificamos qual índice um elemento está na tupla

print(meses.index('Ago'))

# Slicing

# Tupla[inicio:fim:passo]

print(meses[0:7])
print(meses[5:13])


# Por quê utilizar Tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro, por ser imutável tem mais segurança

# Copiando uma tupla para outra

tupla = 1, 2, 3
nova = tupla # Na tupla não temos o problema de Shallow Copy

print(tupla)
print(nova)

outra = 4, 5, 6
print(outra)

nova = nova + outra
print(nova)
print(tupla)
print(outra)
"""

