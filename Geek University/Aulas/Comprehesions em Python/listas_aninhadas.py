"""
Listas aninhadas

- Algumas linguagens de propgramação possuem uma estrutura de dados chamadas de arrays:
    -Unidimensionais (Arrays/vetores)
    - Multidimensionais (Matrizes)

Em Python, nós temos as listas (Que seria arrays em outras linguagens)

numeros = [1, 2, 3, 4, 5]

# Exemplos

listas = [[1, 2 ,3],[4, 5, 6], [7, 8, 9]]  #É uma lista de listas -
                                #Seria um exemplo de Matriz 3 x 3

print(listas)

print(type(listas))

print(listas[0][2])
print(listas[2][1])

# Como fazemos para acessar os dados?

print(listas[1])

teste = [lista * 2 for lista in listas]

print(teste)

# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

print("""
""")
# List compreenshion

[[print(valor) for valor in lista] for lista in listas]

"""

# Outros exemplos

# Gerando um tabuleiro 3 x 3

tabuleiro = [[numero for numero in range(1,11)] for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para jogo da velha

velha = [['x' if numero % 2 == 0 else 'o' for numero in range(1,5)] for tabela in range(1)]
print(velha)

# Gerando valores iniciais

print([['*' for numer in range(1,4)] for tes in range(1,4)])