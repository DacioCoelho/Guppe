"""
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

"""

nome_usuario = str(input('Digite seu nome: '))

nome_maisculo = nome_usuario.upper()

print(nome_maisculo)

nome_invertido = nome_maisculo[::-1]

print(nome_invertido)

nome_maisculo_invertido = ' '.join(reversed(nome_maisculo.split()))

print(nome_maisculo_invertido)
"""
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
"""

nome = 'Dácio'