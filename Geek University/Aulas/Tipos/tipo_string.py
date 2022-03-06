"""
Tipo String

Em Python, um dado é considerado String sempre que:

- Estiver entre áspas simples -> 'uma string', '234', 'a', 'True', '42.3'

- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"

- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

print('Ana')
print(type('ana'))
print(type('''ana'''))

"""

#- Estiver entre aspas duplas triplas -> """uma string"""", """234"""", """a"""", """True""", """42.3"""



"""
O mais comum é colocar aspas simples.

\n é utilizado para pular uma linha (Como se fosse o enter)

nome = "Gina'Bar"
print(nome)

nome1 = "Gina' \n Bar"
print(nome1)
print(type(nome))
print(type(nome1))


print(dir(nome))
print(nome.upper()) #upper -> para maisculo
print(nome.lower()) #lower -> para minusculo
print(nome.split()) #split -> pega as palavras e coloca em uma lista.
                    # ['Dácio', 'Coelho']
                    # ['D', 'à', 'c', 'i', 'o', ' ', 'C', 'o', 'e', 'l', 'h', 'o']
                    # [ 0    1    2    3    4    5    6    7    8    9    10   11]
print(nome[0:5]) # Slice de string
print(nome[6:12]) # Slice de string
print(nome)
print(nome.split()[0])
print(nome.split()[1])
"""

nome = 'Dácio Coelho'

#print(nome[::-1]) # [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta1, in <module>
#AttributeError: 'str' object has no attribute 'reverse'
'Ana Cláudia Dias Malta'

                  #Inversão da string Pythônico

print(nome.replace('o', 'e')) #Dácie Ceelhe

help(type)
dir(type)
