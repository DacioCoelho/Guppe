"""
Faça um programa para imprimir
"""

def triangulo(n: int):
    for i in range(1, n + 1):
        for i in range(1, i + 1):
            print(i, end='   ')
        print(' ')

print(triangulo(20))