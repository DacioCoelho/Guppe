"""
Funções com parâmetros ( de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
    - Não possuem entrada;
    - Não possuem saída;
    - Possuem entrada, mas não possuem saída;
    - Não possuem entrada, mas possuem saída;
    - Possuem entrada e saída;

#   Refatorando uma função

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

def quadrado(numero):
    # return numero * numero
    return numero ** 2 # Esses dois tem o mesmo resultado

print(quadrado()) # Quando não se coloca o número na função, teremos um TypeError.

print(quadrado(2))
print(quadrado(8))
print(quadrado(5))

print(type(quadrado))


# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!')
    print(f'Viva {aniversariante}')

nome = input()
cantar_parabens(nome)

cantar_parabens('Patricia')


# Funções podem ter n parametros de entrada.
# Ou seja podemos receber como entrada em uma função quantos parâmetros forem necessários
# Eles são separados por vírgula.

# Exemplo

def soma(a, b):
    return a + b

def multiplicar (num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(5,8))
print(soma(8, 6))

print(multiplicar(5, 8))
print(multiplicar(8, 6))

print(outra(2, 3, 'Dácio '))
print(outra(1, 4, 'ABDQ '))

# Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

    # print(soma(5, 7 , 8)) #Teremnos umn TypeError
    # print(soma(5)) #Teremnos umn TypeError

# Nomeando parâmetros

def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'

print(nome_completo('Dácio','Coelho'))

print('Qual o seu nome?')
nome = input()
print('Qual o seu sobrenome?')
sobre = input()
print(nome_completo(nome, sobre))

# A diferença entre parâmetro e Argumento

# ParÂmetro são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parÂmetros importa.

nome = 'Dácio'
sobrenome = 'Coelho'
print(nome_completo(nome, sobrenome))
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizamos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.

print(nome_completo(string1= 'Henrique', string2= 'Monteiro'))
print(nome_completo(string2= 'Monteiro', string1= 'Henrique'))

# Erro comun na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3 , 4, 5, 6, 7]

print(soma_impares(lista))
"""

