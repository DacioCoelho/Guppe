"""
Funções com parâmetro padrão - > (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo onde a função de passagem de parametro seja opcional:

print(' Dácio')

print()

# Exemplo onde a passagem de parâmetro e obrigatória:
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # Gera um TypeError, pois o parametro aqui é obrigatório

def exponecial(numero=4, potencia=5): # Colocar o valor padrão, caso esse valor não seja definido
    # o programa define o padrão definido
    #Se o usuário passar dois argumentos, o primeiro sera atribuido ao numero e o segundo a potência
    return numero ** potencia

print(exponecial(2, 3))
print(exponecial(3, 2))

print(exponecial(3)) # Por padrão eleve ao quadrado
print(exponecial(3, 5)) # Eleva a potencia informada pelo usuário
print(exponecial()) # Caso não defina nenhum  argumento e tenha na função definido os padrões,
# ela ira fazer como indicado

OBS: eM FUNÇÃO pYTHON, OS PARÂMETROS COM VALORES DEFAULT (PADRÃO) DEVEM SEEMPRE ESTAR NO FINAL DA DECLARAÇÃO.

def teste(num=3, potencia): # Dessa forma irá dar erro
    return num ** potencia


def teste(potencia, num=3): # Dessa forma irá dar erro
    return num ** potencia
print(teste(1, 5))


# Outros exemplos mais complexo

def mostra_informação(nome= 'Dácio', instrutor= False):
    if nome == 'Dácio' and instrutor:
        return 'Bem vindo meu querido'
    elif nome== 'Dácio':
        return 'Eu pensei que você era o Dácio'
    else:
        return f'Você precisa se cadastrar, {nome}'

print(mostra_informação())
print(mostra_informação('Pedro'))
print(mostra_informação('Dácio', instrutor=True))

# Por quê utilizar parâmetros com valores default
    - Nos permite mais flexibilidade nas funções;
    - Evita erros com parâmetros incorretos;
    - Nos permite trabalhar com exemplos mais legíveis de códigos

# Quais tipos de dados podemos utilizar como valores Default
    - Qualquer tipos de dados:
        * Numeros, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;


# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variavéis locais

instrutor = 'Geek' # Variavel global, pós não faz parte de escopo de nenhuma variavel

def diz_oi():
    instrutor = 'Dácio' # Variavel Local
    return f' Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variavel local com o mesmo nome da variavel global, a local tem preferência

def diz_oi():
    prof = 'Dácio' # Variavel local, só é reconhecida dentro do bloco
    return f'Oi {prof}'

print(diz_oi())

print(prof) # Ao solicitar imprimir a variavel é impossivel, por ela ser local # NameError

# Atenção com variaveis globais (Se puder evitar, evite)
total = 0

def incrementa():
    total = total + 1 # A variavel local está sendo utilizada para processamento sem ter sido inicializada
                    # Gera um UnboundLocalError
    return total

print(incrementa())

total = 0

def incrementa():
    global total # É necessário avisar  para o Python que vamos utilziar a variavel global
    total = total + 1 # A variavel local está sendo utilizada para processamento sem ter sido inicializada
                    # Gera um UnboundLocalError
    return total

print(incrementa())   # 1
print(incrementa())   # 2
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador # É uma variavel não global
        contador = contador + 1
        return contador
    return dentro()

print(fora())
