"""
Jogo da forca
"""

nome = input('Digite seu nome: ')
palavra = 'Esternocleidomastoide'.upper()

print(f'Olá {nome}, seja bem vindo ao Jogo da Forca.')
print('Você terá que descobrir a palavra, antes de ser enforcado, você tem 6 tentativas')

print('A palavra é: ', end='')

for letra in palavra:
    print(f'_ ', end='')

conjunto_letras_palavra = set(palavra)
conjunto_letras_digitadas = set()
erros = 0

while (not conjunto_letras_palavra.issubset(conjunto_letras_digitadas)) and erros < 7:
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavra:
        print('A palavra é: ', end=' ')
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra}', end=' ')
            else:
                print('_ ', end=' ')
    else:
        erros += 1
        print(f'-> Erro {erros} de 6. Tente de novo!')

if erros < 7:
    print('Parabéns, você ganhou!!!!!')
else:
    print(f'Não foi dessa vez {nome}!!')



