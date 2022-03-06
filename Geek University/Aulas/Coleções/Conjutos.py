"""
Conjuntos

Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.

Em Python, os conjuntos são chamados de sets.

Dito isto, da mesma forma que na matemática:

- Sets (Conjuntos) não possuem números duplicados;
- Sets (Conjuntos) não possuem valroes ordenados;
- Elementos não são acessados via índice, ou seja, conjuhntos não são indexados;

Conjuntos são bons para se utilziar quan do precisamos armazenar elementos mas não
nos importamos com a ordenação deles. Quando não precisaos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários( em Python:
    - Um dicionário tem chave/valor;
    - Conjunto tem apenas valor

    # Definindo um conjunto:
# Forma 1

s = set({1, 5, 6 ,7 , 3, 4, 6, 7, 8}) #Repare3 que temos valores repetidos

print(s)
print(set)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar
# erro e não faz parte do conjunto

# FORMA 2
s = {1, 5,3, 6, 7, 8, 9, 7, 6, 7}

print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
    # Importante lembrar que além de não termos valores duplicados, não temos ordem.


# Listas aceitam valores duplicados com isso temos 10 elementos
lista = [99, 25, 14, 57, 2, 2, 45, 25, 78, 99]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados com isso temos 10 elementos
tupla = (99, 25, 14, 57, 2, 2, 45, 25, 78, 99)
print(f'Tupla: {tupla}com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas com isso temos 7 elementos
dicionário = {}.fromkeys([99, 25, 14, 57, 2, 2, 45, 25, 78, 99], 'dict')
print(f'Dicionário: {dicionário} com {len(dicionário)} elementos')

# Conjuntos não aceitam valores duplicados, com isso temos 7 elementos
conjunto = {99, 25, 14, 57, 2, 2, 45, 25, 78, 99}
print(f'Conjunto: {conjunto}com {len(conjunto)} elementos')

Lista: [99, 25, 14, 57, 2, 2, 45, 25, 78, 99] com 10 elementos
Tupla: (99, 25, 14, 57, 2, 2, 45, 25, 78, 99)com 10 elementos
Dicionário: {99: 'dict', 25: 'dict', 14: 'dict', 57: 'dict', 2: 'dict', 45: 'dict', 78: 'dict'} com 7 elementos
Conjunto: {2, 99, 45, 14, 78, 25, 57}com 7 elementos

# Assim como todo outro conjunto em Python podemos colocar tipos de dados misturados em Sets

s = {1, 'f', True, 75,  'd', 7}
print(s)
print(type(s))

# Podemos iterar em um set normalmente:

for valor in s:
    print(valor)


# Usos interessantes com Sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
#informam manualemnte a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'São Paulo', 'Belo Horizonte', 'Belo Horizonte',  'Rio de Janeiro']

print(cidades)
print(len(cidades))

# Precisamos saber quantas cidades distintas temos:

cadastro = set(cidades)
print(cadastro)
print(type(cadastro))
print(len(cadastro))

# Adicionando e removendo elementos em um conjunto

s = {1, 2, 3}

s.add(4)
print(s)
s.add(4) # Duplicidade não gera erro
s.add(5)
print(s)
s.remove(5) # Não é indice, removemos o valor a ser removido.
# OBS: Caso o valor não seja encointrado será gerado o valor KeyError
print(s)
s.discard(4) # Com o discard nenhum erro é gerado caso seja apagado um valor que não existe
print(s)

# Copiando um conjunto para outro

s = {1, 2, 3, 4}

# Deep Copy
novo = s.copy()
print(novo)

novo.add(5)
print(novo)
print(s)

# Shallow Copy

novo = s
print(novo)
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo esudantes do curso Python
        # Contendo estudantes do curso Java

estudantes_python = {'Henrique', 'João', 'Leticia', 'Ana Clara'}

estudantes_java = {'Marcos', 'Ilhiuana', 'Xingu', 'Henrique', 'Ana Clara'}

# OBS: Alguns alunos estão presentes em ambos os conjuntos.

# Pre4cisamos gerar um conjunto com estudantes únicos

#   FORMA 1 - Utilizando Union

unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)


# FORMA 2 - Utilizando o caractere pipe

unicos2 = estudantes_java|estudantes_python
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# FORMA 1 - Utilizando intersection

ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# FORMA 2 - Utilizando o &
ambos2 = estudantes_java & estudantes_python
print(ambos2)


estudantes_python = {'Henrique', 'João', 'Leticia', 'Ana Clara'}

estudantes_java = {'Marcos', 'Ilhiuana', 'Xingu', 'Henrique', 'Ana Clara'}

# Gerar um conjunto de estudantes que só estão em um curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java

# Soma*, Valor Máximo, Valor Mínimo* e Tamanho
# * Se os valroes são inteiros oui reais

s = {1, 5, 7, 8, 6 ,4 ,5 ,3}
print(sum(s))
print(min(s))
print(max(s))
print(len(s))
"""

