# Caixa eletrônico

saque = int(input('Quanto você gostaria de sacar:'))

nota_1_str = nota_5_str = nota_10_str = nota_50_str = nota_100_str = 0

nota_1_int = saque // 1
nota_5_int = (saque // 1) + 4
nota_10_int = saque // 10
nota_50_int = (saque // 10) + 40
nota_100_int = saque // 100

partes_numericas = 0

nota_100_int, saque = divmod(saque, 100)

if nota_100_int == 1:
    nota_100_str = '1 nota de 100'
    partes_numericas += 1
elif nota_100_int > 1:
    nota_100_str = f'{nota_100_int} notas de 100'
    partes_numericas += 1

nota_50_int, saque = divmod(saque, 50)
if nota_50_int == 1:
    nota_50_str = '1 nota de 50'
    partes_numericas += 1
elif nota_50_int > 1:
    nota_50_str = f'{nota_50_int} notas de 50'
    partes_numericas += 1

nota_10_int, saque = divmod(saque, 10)
if nota_10_int == 1:
    nota_10_str = '1 nota de 10'
    partes_numericas += 1
elif nota_10_int > 1:
    nota_10_str = f'{nota_10_int} notas de 10'
    partes_numericas += 1

nota_5_int, saque = divmod(saque, 5)
if nota_5_int == 1:
    nota_5_str = '1 nota de 5'
    partes_numericas += 1
elif nota_5_int > 1:
    nota_5_str = f'{nota_5_int} notas de 5'
    partes_numericas += 1

nota_1_int, saque = divmod(saque, 1)
if nota_1_int == 1:
    nota_1_str = '1 nota de 1'
    partes_numericas += 1
elif nota_1_int > 1:
    nota_1_str = f'{nota_1_int} notas de 1'
    partes_numericas += 1

if partes_numericas == 0:
    print('Serviço não possível.')
elif partes_numericas == 1:
    print(nota_100_str + nota_10_str + nota_50_str + nota_5_str + nota_1_str)
elif partes_numericas == 5:
    print(f'{nota_100_str}, {nota_50_str}, {nota_10_str}, {nota_5_str} e {nota_1_str}')
elif partes_numericas == 4:
    if nota_100_str != '':
        print(f' {nota_50_str}, {nota_10_str}, {nota_5_str} e {nota_1_str}')
    elif nota_50_str != '':
        print(f' {nota_100_str}, {nota_10_str}, {nota_5_str} e {nota_1_str}')
    elif nota_10_str != '':
        print(f' {nota_100_str}, {nota_50_str}, {nota_5_str} e {nota_1_str}')
    elif nota_5_str != '':
        print(f' {nota_100_str}, {nota_50_str}, {nota_10_str} e {nota_1_str}')
    elif nota_1_str != '':
        print(f' {nota_100_str}, {nota_50_str}, {nota_10_str} e {nota_5_str}')
else:
    print(f' {nota_100_str}, {nota_50_str}, {nota_10_str}, {nota_5_str}, {nota_1_str}')


