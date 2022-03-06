"""
Dicionários
"""

linguas = {'br': 'Brasil', 'en': 'Inglês'}

print(linguas)

print(linguas['br'])
print(linguas['en'])

print('br' in linguas)
print('es' in linguas)

print(8 in list(range(10)))
print(11 in list(range(10)))

linguas['es'] = 'Espanol'
print('es' in linguas)
print(linguas['es'])

linguas['es'] = 'Espanhol'
print(linguas['es'])

#ITERAÇÃO

for chave in linguas:
    print(chave)

for jo in linguas.values():
    print(jo)

for suco in linguas.items():
    print(suco)

# REMOVER ELEMENTOS DO DICIONÁRIO:
linguas.pop('es')
print(linguas)

del linguas['en']
print(linguas)