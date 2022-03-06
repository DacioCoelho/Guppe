lista = [1, 4.5, True, []]
type(lista)

print(lista[0]) # Vai retornar o número 1
lista[1] # Vai retornar o número 4.5
lista[2] # Vai retornar o número True
lista[3] # Vai retornar o número []

len(lista)  # Para saber o tamanho de uma lista

lista[0] # Vai retornar o número 1
print(lista[-3]) # Vai retornar o número 4.5
lista[-2] # Vai retornar o número True
lista[-1] # Vai retornar o número []

# Fatiamento
print(lista[0:2])
# 1, 4.5
lista[1:3]
# 4.5, True

#Criando uma lista utilizando range

numero = list(range(1,11))
print(numero)
pares = numero[1: 7: 2]
print(pares)
