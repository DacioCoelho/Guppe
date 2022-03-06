"""
Estrutura de repetição: FOR
"""

soma = float(input('Digite um número:'))
for n in range(2,6):   #Seja x um numero inteiro, tal que x está dentro de range
    soma += float(input('Digite um número:'))
    media = soma / n

    print(f'A soma dos números é é: {soma} e a média é {media}')