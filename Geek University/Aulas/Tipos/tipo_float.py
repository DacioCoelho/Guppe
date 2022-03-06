"""
Tipo Float

Tipo real, decimal

Casas decimais

É usado quando precisamos de precisão

OBS: O separador de casas decmais na programação é o ponto e não a vírgula
"""
# Errado do ponto de vista do Float, mas gera uma Tuple
valor = 1,44
print(valor)
print(type(valor)) #-> Não é um valor é decimal e sim um tuple

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor)) # É um valor decimal, conhecido como Float

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)

# Podemos converter um float para um int

"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
