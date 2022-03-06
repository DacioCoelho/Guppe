"""
Mapas - conhecidos em Python como dicionários.

Dicionários em Pythonm são representados por chaves.

# Iterar sobre dicionários

for chave in receita:  # Forma de encontrar o mês, o primeiro elemento presente no dicionário
    print(chave)

for chave in receita: # Forma de encontrar o valor, o último elemento presente no dicionário
    print(receita[chave])

for chave in receita:
    print(f'EM {chave}, eu recebi {receita[chave]}')

# Acessando as chaves:

print(receita.keys())

for chave in receita.keys(): # Modo Pythonico de fazer a ação
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)


# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'A chave é {chave} e o valor é {valor}')


# Soma*, Valor Máximo, Valor Mínimo* e Tamanho
# * Se os valroes são inteiros oui reais

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita.values()))
"""

receita = {'jan':100, 'fev': 142, 'mar':150}
print(receita)
