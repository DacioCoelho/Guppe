"""
Loop for
Loop - Estrutura de repetição
For - Uma dessas estruturas

#Em Python

for item in interavel:
    //execução loop

Utilizamos Loops para iterar sobre sequências ou valores iteráveis.

Exemplos de interáveis
- String
    nome = 'Dácio Coelho'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
nome = 'Dácio Coelho'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista
"""
# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Interando em uma lista)
for numeros in lista:
    print(numeros)

range(valor_inicial, valor_final)
OBS: O valor final não inclusive.
Range(1, 5)
1
2
3
4
5 - Não entra na lista

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1,10):
    print(numero)
    
Enumerate

((0, 'D'), (1, 'Á'), (2, 'C'), (3, 'I'), (4, 'O'), (5, ' '), (6, 'C'), (7, 'O')....

for indice, letra in enumerate(nome):
    print(nome[indice]

for indice, ltra in enumerate(nome):
    print(letra)
    
for _, letra in enumerate(nome):
    print(letra)
    
OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um under line(_)

for valor in enumerate(nome):
    print(valor)
    print(valor[0])
    print(valor[1])


qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')

for letra in nome:
    print(letra, end='')


Tabela de Emoji Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
# Original: U + 1F63B
# Modificado para Python: U0001F63B

for _ in range(3):
    for num in range(5, 20):
        print('\U0001F63B' * num)

