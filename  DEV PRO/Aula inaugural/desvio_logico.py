idade = 55

if idade < 18:
    print(f'Menor de idade: {idade}')
elif idade == 18: # Você pode ter quantos elif quiser em um desvio lógico
    print(f'Você tem 18 anos.')
elif idade >= 65:
    print(f'Você tem {idade} anos, é considerado uma pessoa idosa.')
else: # Se você quiser, você também concluir com else
    print(f'Você tem {idade} anos, então é maior de idade.')
