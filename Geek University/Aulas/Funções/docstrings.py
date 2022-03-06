"""
Docstrings - Aspas duplas ou triplas

É uma forma de escrever algo que seja essencial para a contrução da programação.

print(help(print)

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

None

OBS:  Para acessar a documentação podemos utilizar o: .__doc__

PODEMOS AINDA FAZER ACESSO A DOCUMENTAÇÃO COM A FUNÇÃO help()
"""

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

def exponecial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de número ou a pontecia informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Número que desejamos gerar o exponencial. Por padrão é 2
    :return: Retorna o expenencial de " número por poténcia"
    """
