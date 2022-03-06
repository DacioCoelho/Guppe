"""
Estrutura de repetição

"""

"""
contar = 0

while contar < 4: #Enquanto (Funciona como desvio condicional) (Util quando você sabe quantas vezes usar seu programa
    print(contar)
    contar += 1
"""
while True:
    try:  #Usado para tentar tratar uma string em número ou o que for solicitado
        numero = int(input('Digite um numero:'))
    except ValueError:
        print('Deve ser um número inteiro')
    else:
        if 0<= numero <= 10:
            print(f' O número informado é {numero}')
            break
        else:
            print(f'O número deve estar entre 0 e 10')







