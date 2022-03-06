def classificar(idade, nome):
    if idade < 18:
        print(f'{nome} você é  menor de idade: {idade}')
    elif idade == 18:  # Você pode ter quantos elif quiser em um desvio lógico
        print(f'{nome} você tem 18 anos.')
    elif idade >= 65:
        print(f'{nome} você tem {idade} anos, é considerado uma pessoa idosa.')
    else:  # Se você quiser, você também concluir com else
        print(f'{nome} você  tem {idade} anos, então é maior de idade.')

classificar(28, 'Dácio')
classificar(88, 'Henrique')
classificar(18,'Ana')
classificar(2, 'João')


idades = [17, 38, 70, 80]
classificar(idades[0], 'Dácio')

for idade in idades:
    print(classificar(idade, 'Dácio'))