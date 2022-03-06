"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidas por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

print(type({})) - <class 'dict'>

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dados;
    - Podemos misturar tipos de dados;

# FORMA 1 - (MAIS COMUM)
paises = {'BR':'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}
print(paises)
print(type(paises))

# FORMA 2 (MENOS COMUM)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))
# Acessando elementos

# FORMA 1 -Acessando via chave, da mesma forma que lista/tupla
print(paises['BR'])
print(paises['PY'])
# print(paises['RU'])
    #obs: Caso tentamos fazer acesso utilizando uma chave que não existe, teremos o erro KeyError

# FORMA 2 - Acessando via get - RECOMENDADO
print(paises.get('BR'))
print(paises.get('RU'))

pais = paises.get('RU')

# Caso o get não entre o objeto com a chave informada será retornado o valor None e não será gerado KeyError
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada.

pais = paises.get('RU', 'Não encontrado')
print(pais)


# Podemos verificar se determinada chave se encontra em um dicionário

print('BR' in paises)
print('Estados Unidos' in paises)  # Estados Unidos não é chave e sim valor
print('RU' in paises)

if 'RU' in paises:
    pais = paises['RU']
    print(pais)

if 'BR' in paises:
    pais = paises['BR']
    print(pais)
    # Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionários, como chaves
# de dicionários.

# Tuplas são por exemplo bastante interessantes de serem utilizadas como cgave de dicionário, pois as mesmas são imutáveis.
localidades = {
    (35.6589, 39.6587): 'Escritório do Dácio',
    (40.7412, 74.0087): 'Escritório do Ana',
    (37.6522, 122.5682): 'Escritório do Henrique',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em Python

receita = {'jan':100, 'fev': 142, 'mar':150}
print(receita)
print(type(receita))

# FORMA 1 - MAIS COMUM

receita['abr'] = 170
receita['mai'] = 100

print(receita)

# FORMA 1

novo_dado = {'jun': 130}

receita.update(novo_dado) # É a mesma coisa que : receita.update({'jun': 130})
print(receita)

# Atualizando dados em um dicionário

# FORMA 1
receita['mai'] = 200
print(receita)

# FORMA 2
receita.update({'mai':100})
print(receita)


# CONCLUSÃO: A forma de adicionar novos elementos em um dicionário é a mesma.

# CONCLUSÃO: Em dicionários NÃO podemos ter chaves repetidas.


# Remover dados de um dicionário

receita = {'jan':100, 'fev': 142, 'mar':150}
print(receita)
# FORMA 1 - FORMA MAIS COMUM

ret = receita.pop('mar')
print(ret)
print(receita)

# OBS: RPrecisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.

# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# FORMA 2

del receita['fev']
print(receita)

# nESTE CASO O VALOR REMOVIDO NÃO É RETORNADO
Carrinho
    Produto 1:
        - nome;
        - quantidade;
        - preço
    Produto 2:
        - nome;
        - quantidade;
        - preço


# 1 - Poderíamos utilizar uma LISTA para isso:

carrinho = []

produto1 = ['Nintendo', 2, 1500.00]
produto2 = ['Xbox', 4, 2000.00]

print(produto1)
print(produto2)

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print(type(carrinho))

# Teriamos que saber qual o indice de cada informação no produto.

# 1 - Poderíamos utilizar uma TUPLA para isso:

produto1 = ('Nintendo', 2, 1500.00)
produto2 = ('Xbox', 4, 2000.00)

carrinho = (produto1, produto2)
print(carrinho)
print(type(carrinho))

# Teriamos que saber qual o indice de cada informação no produto.

# PODERIAMOS UTILIZAR UM DICIONÁRIO PARA ISSO
carrinho = []

produto1 = {'nome': 'Nintendo', 'quantidade': 2, 'preço': 1500.00}
produto2 = {'nome': 'Xbox', 'quantidade': 4, 'preço': 2000.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print(type(carrinho))

# Dess forma facilmente adicionamos e removemos produtos no carrinho.
# e em cada produto podemos ter a certeza sobre cada informação

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

# Métodos de dicionários.

#dir({})
#['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__g
#t__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__
#', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', '
#popitem', 'setdefault', 'update', 'values']

d = dict(a=1, b=2, c=3, d=4, e=5)
print(d)
print(type(d))

# Limpar o dicionário (Zerar os dados)

d.clear()
print(d)


# Copiando um dicionário para outro
# FORMA 1 -Deep Copy

novo = d.copy() # Deep Copy - Se refere a uma copia sem danificar o original
print(novo)

novo['f'] = 6

print(d)
print(novo)

# FORMA 2 - Shallow Copy

novo = d

novo['f'] = 6

print(d)
print(novo)
"""

# FORMA NÃO USUAL DE CRIAÇÃO DE DICIONÁRIO

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'idade'], 'desconhecido')
print(usuario)
print(type(usuario))

# o Método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

usuario = {}.fromkeys(range(1,11), 'novo')
print(usuario)
print(type(usuario))


