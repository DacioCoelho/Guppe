linguas = {'pt': 'Portugues', 'en': 'Inglês'}
print(linguas['pt'])

linguas['es'] = 'Espanhol'

print(linguas)

for chaves in linguas:
    print(chaves)

for valores in linguas.values():
    print(valores)

for chave, valor in linguas.items():
    print(chave, valor)