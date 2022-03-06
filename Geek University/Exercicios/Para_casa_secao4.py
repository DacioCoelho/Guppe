"""
Questão 5 - não sei fazer

nome = 42
print(nome)
print(type(nome))

nome1 = 42.5
print(nome1)
print(type(nome1))

nome = 2
nome1 = 5
nome2 = 8
print(nome+nome1+nome2)

nome = 45.5
print(nome*2)
print(nome**2)

C = 30
F = C*(9.0/5.0)+32.0
print(F)

F = 80
C = 5.0*(F-32.0)/9.0
print(C)

C = 30
K = C + 273.15
print(K)

K = 120
M = K/3.6
print(M)

K = 30
M = K/1.61
print(M)

num = 20
print(num + 1)
print(num - 1)
"""
"""
valor1 = 10
valor2 = 20
valor3 = 15

qv1 = valor1 ** 2
qv2 = valor2 ** 2
qv3 = valor3 ** 2

Soma = qv1 + qv2 + qv3
print(Soma)
print(f'A Soma do quadrado dos 3 valores é {Soma}')


nota1 = 8.5
nota2 = 7.5
nota3 = 10
nota4 = 5.5

media = (nota1 + nota2 + nota3 + nota4)/4

print(media)

real = 250
dolar = 5.56

cotacao = real / dolar
print(cotacao.__int__())
4

num = 20
print(num + 1)
print(num - 1)

print(f'O {num} tem como antecessor o número { num - 1 } e como sucessor o número { num + 1 }')

num = 20
print(f'A soma do sucessor é {(num + 1)*3} e a soma do antecessor é {(num - 1)*2} ')


lado = 30
área = lado * 2
print(f'O quadrado de lado {lado} é igual à {área}m2')


import math
a = 55
b = 75
hipotenusa = math.sqrt(a**2+b**2)
print(hipotenusa)

altura = 100
raio = 50
V = math.pi * raio ** 2 * altura
print(V)

produto = 80
desconto = produto * 0.88
ajuste = produto * 1.12
print(desconto)
print(ajuste)
print(f'O produto custa {produto} reais, pagando a vista com desconto de 12%, fica em {desconto} reais e parcelado fica em {ajuste.__int__()} reais')

Premio = 780_000_000
ganh1 = Premio * 0.46
ganh2 = Premio * 0.32
ganh3 = Premio - ganh2 - ganh1

print(ganh1.__int__(), ganh2.__int__(), ganh3.__int__())

dias = 25
liq = (30 * dias) * 0.92
print(liq)
print(f'O salário ordenado é de: {liq : .2f}')

vh = 30
ht = 8 * 5 * 4
sal = (vh * ht)*1.10
print(sal)

Henrique = 1_000
grati = Henrique * 0.05
impos = Henrique * 0.07

sal = 1000 + grati - impos
print(sal)
print(grati)
print(impos)

valor = 100
desconto = valor * 0.90
parcela = valor / 3
comi = desconto * 0.05
comipar = valor * 0.05
print(parcela)
print(comi)
print(comipar)


import math
altura = 20
objetivo = 1000
degraus = objetivo / altura
print(degraus)


segundos = 45_000
minutos = segundos/60
hora = segundos/3600

print(minutos)
print(hora)
print(f'{segundos} é igual a {minutos} minutos e {hora} horas')

"""

idade = input(f'Qual a sua idade?')
print(f'Sua idade é {idade} anos e você nasceu em {2021 - int (idade)}')
