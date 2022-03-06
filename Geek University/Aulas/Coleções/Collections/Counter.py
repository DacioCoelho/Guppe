"""
Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

É conhecido por High-performance Container Datetypes

Container - A partir de um tipo de dados posso adicionar várias coisas.

Counter - Recebe um iteravel como parâmetro e cria um objeto do tipo Colletions Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrência
desse elemento.


# Utilizando o Counter

from collections import Counter   # Para utilizar o Counter é necessário fazer o import

# EXEMPLO 1

# Podemos usar qualquar iteravel (Lista, dicionartio...)
lista = [1, 2, 1, 5, 7, 1, 8, 4, 8, 5, 5, 1, 2, 1, 5, 7, 8, 8]

res = Counter(lista)
print(type(res))

print(res)

# Counter({1: 5, 5: 4, 8: 4, 2: 2, 7: 2, 4: 1})

# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantiodade de ocorrências.

 # Exemplo 2
print(Counter('Dácio Coelho'))

# Para cada um dos caracters ele cria as ocorrências.
"""

from collections import Counter

# EXEMPLO 3

texto = """ League of Legends (abreviado como LoL) é um jogo eletrônico online gratuito,
 do gênero batalha multijogador, 
desenvolvido e publicado pela Riot Games em 2009,[3] para os sistemas Microsoft Windows e Mac OS X, 
inspirado no modo Defense of the Ancients[4] do jogo Warcraft III: The Frozen Throne.[5]

Em League of Legends, os jogadores assumem o papel de "invocadores", que controlam campeões com habilidades únicas,
 que formam um time e lutam contra o time adversário de outros invocadores ou controlados pelo computador.
  No modo mais popular do jogo, o objetivo de cada time é destruir o Nexus da equipe adversária, 
  uma construção localizada na base e protegida por outras estruturas. Cada partida de League of Legends é 
  distinta, pois os campeões sempre começam fracos e progridem através da acumulação de ouro e da experiência 
  ao longo do jogo"""

palavras = texto.split()

print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências
print(res.most_common(5))
print(res.most_common(10))

# docs.python.org/3/library/collections.html