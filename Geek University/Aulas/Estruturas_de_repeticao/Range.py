"""
Ranges - Função auxiliar

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conehcer o range para trabalhar com loops for

Ranges - são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (ínicio padrão 0, e passo de 1 em 1)

# Forma 1
for num in range(11):
    print(num)

# Forma 2 range (valor_de_ínicio, valor_de_parada)
for num in range(5, 8):
    print(num)

# Forma 3 (valor_de_inicio, valor_de_parada, passo)
# valor_de_parada não inclusive (ínicio padrão 0, e passo especificado pelo usuário)
for num in range(5, 51, 5):
    print(num)

# Forma 4 - Inversa (valor_final, valor_de_parada, passo)

for num in range(10, -1, -1):
    print(num)
"""

