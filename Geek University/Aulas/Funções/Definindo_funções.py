"""
Funções ->

- Função são pequenas partes de códigos que realizam tarefas especificas;
- Pode ou não receber entrada de dados e retornar uma saida de dados;
- Muitis uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada;

- Já utilizamos várias funções:
    - print()
    - len()
    - max()
    - min()
    - count()


# Exemplo de utilização de funções

cores = ['verde', 'branco', 'azul', 'amarelo']

# Utilizando uma função integrada (Built-in) do Python print()

print(cores)

cores.append('preto')

print(cores)

cores.clear() # Quando alguma função depender de alguém é necessário colocar o ponto entre elas para interligar
print(cores)

# print(help(print)

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas como definir funções


Em Python a forma geral de definir uma função é:

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao
    
Onde: 
nome_da_funcao -> SEMPRE com letras minuscúlas, e se for nome composto, separado por underline( Snakee Case)
parametros_de_entrada -> São Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Para definir uma função, utilizamos a palavra reservada 'def'. informando ao Python que estamos definindo uma função
Também abrimos o bloco de código com o já conehcido dois pontos ':' que é utilizado em Python para definir blocos
"""

# Definindo a primeira função

def diz_oi():
    print('oi!')

""" 
OBS: 

1- Veja que, dentro das funções podemos utilizar outras funções;
2 - Veja que, nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que está função não retorna nada;
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
Atenção:

Nunca esqueça de utilizar o parenteses ao executar uma função.

# Exemplo certo

diz_oi()

# Exemplo errado

diz_oi    iu   diz_oi ( )
"""

# Exemplo 2

def cantar_parabens():
    print('Parabens para você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida!')


#for n in range(4):
#    cantar_parabens()

# Em Python podemos inclusive criar variaveis do tipe de uma função e executar esta função através da variavel

canta = cantar_parabens

canta()