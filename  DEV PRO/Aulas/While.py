"""
While = laço
"""

nome = 'Dácio'

i = 0  # Criação de uma variavel
while i < len(nome): #O While executa o conjunto de linhas, enquanto a expressão for verdadeira.
    print(nome[i])
    i += 1

for v in nome:
    print(v)

for i in range(len(nome)):
    print(i, nome[i])

for i, v in enumerate(nome):   # COMANDO MAIS LIMPO
    print(i, v)