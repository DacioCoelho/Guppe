"""
ultimo = 0
penultimo = 0

n = int(input('Qual a variavel você quer?'))

while (ultimo < n):
    print(ultimo)
    ultimo = ultimo + penultimo
    penultimo = ultimo - penultimo

    if (ultimo == 0):
        ultimo = ultimo + 1
"""

