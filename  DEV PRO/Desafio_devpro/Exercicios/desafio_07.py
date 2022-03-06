notas = []

while True:
    entrada = input('Digite um número, ao termino do lançamento digite -1:   ')
    if entrada == '-1':
        break
    notas.append(float(entrada))
tamanho = len(notas)

print(f'Foram lidas {notas} notas')
print(' '.join([str(nota) for nota in notas]))

notas.reverse()
print(notas)

for nota in notas:
    print(nota)

soma = sum(notas)
print(f'A soma das notas é: {soma}')

media = soma / tamanho
print(f'A média das notas é: {soma / tamanho}')

print('Notas acima da média: ')

print(' '.join([str(nota) for nota in notas if nota > media]))


print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Encerrado o programa de estatistica de notas')



