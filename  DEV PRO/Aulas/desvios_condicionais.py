"""
Só acontece, se determinada condição atende a demanda
"""

idade = 19

if idade < 18:
    print(f'Você tem {idade} anos, logo é menor de idade.')
elif idade > 18:
    print(f'Você tem {idade} anos. Logo é maior de idade.')
else:
    print('Você tem 18 anos.')