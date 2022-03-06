"""
Listas

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagem C/JAVA: Arrays
    - Possuem tamanho e tipos de dado fixo;
    Ou seja, nestas linguagens se você criair um array do tipo int e com tamanho 5, esse array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Em Python:
- Dinâmico: Não possui tamanho fixo; Você cria a lista e vai colocando elementos;
- Qualquer tipo de dado: Não possuem tipos de dados fixos; podemos colocar qualquer tipo de dado.

As listas em python são representadas por colchetes: []



type([])

lista1 = [1, 99, 78, 5, 19, 26, 28]

lista2 = ['D', 'a', 'c', 'i', 'o', ' ', 'C', 'o', 'e', 'l', 'h', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list('Dacio Coelho')

lista6 = lista1 + lista2

lista7 = lista2

lista8 = ['Brain','Master','-','Treinamento', 'Mental']

# Podemos facilmente chegar se determinado valor está contido na lista.
num = 'D'
if num in lista2:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista:
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# Podemos facilmente contar o número de ocorrências de uma valor em uma lista
print(lista1.count(1))
print(lista5.count('o'))

# Adicionar elementos em listas


Para utilizar elementos em listas, utilizamos a função append


print(lista1)
lista1.append(44)
print(lista1)
lista1.append(55)
print(lista1)
lista1.sort()
print(lista1)

#OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.apeend(12, 33, 48, 98) # Erro

lista1.append([11, 22, 33, 44])
lista1.extend([111,22, 222, 333])
print(lista1)
lista1.count(111)
print(lista1)

# .extend - é utilizado para colocar mais de um valor e não um valor único.
# .append - é utilizado para colocar um único valor.


# Podemos inserir um novo elemento na lista informando a posição do índice.
# OBS: Não substituio o valor inicial, apenas desloca ele para a direita.
lista1.insert(2, '13')
print(lista1)
lista1.insert(2,55)
print(lista1)

print(lista1)
lista1.reverse()
print(lista1)
print(lista1[::-1])

# Utilizando o .len -> podemos contar quantos elementos temos dentro da lista.
print(len(lista2))
print(len(lista1))
print(len(lista4))
print(len(lista5))
print(len(lista6))

# Podemos facilmente remover o último elemento de uma lista
# OBS: O pop não somente remove o últmo elemento, mas também retorna

print(lista5)
lista5.pop()
print(lista5)

#Podemos remover um elemento pelo indice
# Obs: Os elementos à direita desse indice serão deslocados para a esquerda.
# OBS: Se não ouver elemento no indice informado, teremos o erro IndexError
lista5.pop(5)
print(lista5)

# Usado para limpar a lista, e zerar ela.
print(lista7)
lista7.clear()
print(lista7)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3, 4]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# OBS: Por padrão, o slpit separa os elementos da lista pelo espaço entre elas.

curso = 'Brain Master - Treinamento de Psicologia do Esporte'
print(curso)
curso = curso.split()
print(curso)
curso = 'Brain-Master-Treinamento-de-Psicologia-do-Esporte'
curso = curso.split('-')
print(curso)


curso = ' '.join(lista8)
print(curso)

# Podemos colocr realmente qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista9 = [1, 2.3, True, 'Dácio', 'c', [1, 2, 3],45778475]
print(lista9)
print(type(lista9))

# Iterando sobre lista

# Exemplo 1 - tudo depende do tipo de dado que é utilizado, se for inteiro, usar números, se for
#string utilizar espaço ou virgulas

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2

carinho = []  #lista vazia
produto = ' '

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carinho.append(produto)

for produto in carinho:
    print(produto)
    
# Criar listas com variavéis
numeros = [1, 2, 3, 4, 5]

#ou
num1 = 1
num2 = 2
num3 = 3
num4 = 4

numeros = [num1, num2, num3, num4]

# Fazemos acesso aos elementos de forma indexada

#           0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])

# Fazer acesso aos elementos de fora indexada inversa
# Para entender melhor o indice negativo, pens a lista como uma roda, pois o final de um
# #elemento está ligado ao ínicio da lista
print(cores[-1]) #branco
print(cores[-2]) #azul

for cor in cores:
    print(cor)
    
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
    

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice,cor)

#>>> cores = list(enumerate(cores))
#>>> cores
#[(0, 'verde'), (1, 'amarelo'), (2, 'azul'), (3, 'branco'), (4, 'vermelho')]
cores = ['verde', 'amarelo', 'azul', 'branco']

# Lista aceita valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(40)
print(lista)

#  Outros métodos não tão importantes mas úteis

# Encontrar o índice de um elemento na lista:

numero = [1, 2, 3, 5, 8, 9, 15, 16, 78, 99,5 ,120, 1000]
Supermercado = ['arroz', 'feijão', 'batata', 'mandioca', 'macarrão', 'ovo', 'legumes']

# Em qual indice da lista está o valor 6 e o arroz, lembrando que o indice se inicia no zero
print(numero.index(5))
print(Supermercado.index('batata'))

# Em qual indice da lista está o valor 6 e o arroz, lembrando que o indice se inicia no zero
print(numero.index(120))
print(Supermercado.index('ovo'))

# OBS: Caso não tenha o elemento na lsita, irá apresentar a mensagem de erro -> ValueError
#print(numero.index(6)) -> Gera erro

# Se tiver números repetidos na lista, ele vai retornar o primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar:
print(numero.index(5))
print(numero.index(5, 4))# Buscando a partir do indice 4

# Podemos fazer busca dentro de um range, ínicio/fim
print(numero.index(5, 4, 12)) # Delimitando o ínicio e o fim do range

# Revisão do slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slicing de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos depois
print(lista[::]) # Indica que quero pegar todos os elementos, não defini um ínicio
print(lista[1:5]) # Indica o ínicio e o fim
print(lista[:5]) # Não indica onde começa, só onde termina
print(lista[1:6:2]) # Indica onde inicia, onde termina e de quanto em quanto pula para o próximo
print(lista[::3]) # Indica de quanto em quanto pula para o próximo número
print(lista[2::3]) # Começa em 2, pula de 3 e 3
print(lista[::-1]) # Para inverter a lista usar o -1, -2, -3 ...
print(lista[::-3])

nome = ['Treinamento', 'Mental', 'Brain', 'Masters']
nome.reverse()
print(nome)

#Soma*, Valor Máximo*, Valor mínimo*, Tamanho
# * - se os valores forem inteiros ou reais

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(sum(lista)) # Soma
print(max(lista)) # Valor Máximo
print(min(lista)) # Valor Mínimo
print(len(lista)) # Tamanho da lista

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacoamento de listas
lista1 = [1, 2, 3]

num1, num2, num3 = lista1
print(num2)

# OBS: Se tivermos mais elementos para desempacotar do que variavéis para receber os valroes, teremos ValeuError
# Se tiver número diferente ou váriaveis, teremos um ValeuError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
lista1 = [1, 2, 3]
print(lista1)

nova = lista1.copy()
print(nova)
nova.append(4)
nova.append(5)
print(lista1)
print(nova)

# Se você apenas igualar uma lista, todas as mudanças que você fizer na lista nova, altera a antiga
# por isso é importante fazer o copy()
# ISSO EM PYTHON É CHAMADO DE DEEP COPY (Cópia profunda)
# QUANDO APENAS COPIAMOS AS LISTAS, A MODIFICAÇÃO REFLETE NAS LISTAS
# EM PYTHON É CHAMADO DE SHALLOW COPY
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Forma 2 - Shallow Copy
lista1 = [1, 2, 3]

novo = lista1
print(novo)
novo.append(6)
print(lista1)