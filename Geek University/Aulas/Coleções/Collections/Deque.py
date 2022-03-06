"""
Módulo Collections - Deque - Lista de alta performace

https://docs.python.org/3/library/collections.html#collections.deque
"""

from collections import deque

# Criando Deques

deq = deque('Dácio Coelh')
print(deq)

# Adicionando elementos no deque

deq.append('o') # ADICIONA NO FINAL

print(deq)

deq.appendleft('Meu nome é: ')
print(deq)

# Romever elementos

print(deq.pop()) # Remove e retorna o último elemento

print(deq)
deq.append('o')

print(deq.popleft())

print(deq)