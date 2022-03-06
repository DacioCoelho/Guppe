def contar_caracters(s):
    """
    Função que conta os cartacteres de uma string

    EX:
    >>> contar_caracters('Dacio')
    a: 1
    c: 1
    d: 1
    i: 1
    o: 1
    >>> contar_caracters('banana')
    a: 3
    b: 1
    n: 2
    :param s: string contada
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}:{contagem}')

if __name__ == '__main__':
    contar_caracters('Dacio')
    print()
    contar_caracters('banana')
