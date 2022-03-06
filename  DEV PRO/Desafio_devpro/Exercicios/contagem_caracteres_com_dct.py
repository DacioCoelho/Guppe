def contar_caracters(s):
    """
    Função que conta os cartacteres de uma string

    EX:
    >>> contar_caracters('dacio')
    {'a': 1, 'c': 1, 'd': 1, 'i': 1, 'o': 1}
    >>> contar_caracters('banana')
    {'a': 3, 'b': 1, 'n': 2}

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    resultado = {}

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            resultado[caracter_anterior] = contagem
            caracter_anterior = caracter
            contagem = 1

    resultado[caracter_anterior] = contagem

    return resultado

if __name__ == '__main__':
    contar_caracters('Dacio')
    print()
    contar_caracters('banana')
"""
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter,0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado
    print(resultado)

if __name__ == '__main__':
    contar_caracters('dacio')
    print()
    contar_caracters('banana')