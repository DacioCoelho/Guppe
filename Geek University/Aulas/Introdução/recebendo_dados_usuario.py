"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples tripla;
- Aspas dupla tripla;

Exemplo:
- Aspas simples -> 'Dácio'
- Aspas duplas -> "Dácio"
- Aspas simples tripla -> '''Dácio'''
"""
# - Aspas dupla tripla -> """Dácio"""

#Entrada de dados
print("Qual o seu nome?")
nome = input() # Input -> Entrada

# Exemplo de print 'antigo' 2.x
#print('Seja bem-vindo(a) %s' %nome)

# Exemplo de print 'moderno' 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo do print 'mais atual' 3.7...
print(f'Seja bem-vindo(q) {nome}')

print("Qual a sua idade?")
idade = input()

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
#print('A %s tem anos' % nome, idade)

# Exemplo de print 'moderno' 3.x
# print('O {0} tem {1} anos'.format(nome, idade))

# Exemplo do print 'mais atual' 3.7...
print(f'O {nome} tem {idade} anos, certo?')
"""
# int(idade) => Cast

Cast é a 'conversão' de um tipo de dado para outro
"""

print(f'O {nome} nasceu em {2021 - int(idade)}')