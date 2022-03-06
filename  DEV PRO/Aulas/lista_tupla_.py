"""
Lista em Python = []


lista = list(range(11))   #Vai criar uma lista de 0 a 10

lista = list(range(1,11))   #Vai criar uma lista de 1 a 10

lista = list(range(1,11,2))   #Vai criar uma lista de 0 a 10, pulando de 2 em 2

lista = list(range(10,0))   #Vai criar uma lista de 10 a 0 de forma descrescente

lista = list(range(10,0, -2))   #Vai criar uma lista de 10 a 0 de forma descrescente de 2 em 2


lista.append(12) #usado para acrscentar algum numero

lista.pop() #usado para retirar algum número

lista.extend([12,14]) #Usado para acrescentar mais de um número

teste = 'Python Pro'

teste.split() #Usado para separar strings

print(teste)

'#'.join(teste)

lista = [1. 1.0, 'Renzo', []]
"""

#TUPLA

tpl = (1, 2) #Para ser tupla é necessário utilizar parenteses e virgula

# É necessário usar a virgula para gerar uma tupla

registro = ('Dácio', 31)

nome, idade = registro

print(nome)
print(idade)

nome, idade, sexo = 'Coelho', 30, "Masculino"
print(nome)
print(idade)

