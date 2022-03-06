"""
Python em 14 dias
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
 Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

string1 = input('Digite uma palavra: ')
string2 = input('Digite uma palavra: ')

tamanho1 = len(string1)
tamanho2 = len(string2)

comparacao_de_tamanhos = 'diferentes'
comparacao_de_conteudo = 'diferentes'

if string1 == string2:
    comparacao_de_tamanhos = 'iguais'
    comparacao_de_conteudo = 'iguais'
elif tamanho2 == tamanho1:
    comparacao_de_tamanhos = 'igual'


print(f'Tamanho de "{string1}": {tamanho1} caracteres')
print(f'Tamanho de "{string2}": {tamanho2} caracteres')

print(f'As duas strings são de tamanhos {comparacao_de_tamanhos}.')
print(f'As duas strings possuem conteúdos {comparacao_de_conteudo}.')