"""
List Comprehesions

Nós podemos adicionar estruturas condicionais lógicas

numeros = [ 1, 2 ,3 ,4 ,5 ,7 , 8 ,9]

pares = [numero for numero in numeros if numero % 2 == 0]

impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

#Exemplo
numeros = range(1,50)

pares = [numero for numero in numeros if numero % 2 == 0]

impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not false = True
pares2 = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1 e 1 em Python é  True
impares2 = [numero for numero in numeros if numero % 2]
print(pares2)
print(impares2)
"""

#EXEMPLO 2
numeros = range(1,12)

res = [numero * 2 if numero % 2 == 0 else numero/1 for numero in numeros]

print(res)
