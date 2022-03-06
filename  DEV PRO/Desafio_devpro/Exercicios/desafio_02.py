numero = int(input('Digite um número:'))

centenas_str = dezenas_str = unidades_str = ''

centenas_int = numero // 100

dezenas_int = numero // 10

unidades_int = numero // 1

partes_numericas = 0

centenas_int, numero = divmod(numero,100)

if centenas_int == 1:
    centenas_str = '1 centena'
    partes_numericas += 1
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'
    partes_numericas += 1

dezenas_int, numero = divmod(numero,10)
if dezenas_int == 1:
    dezenas_str = '1 dezena'
    partes_numericas += 1
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'
    partes_numericas += 1

unidades_int, numero = divmod(numero,1)
if unidades_int == 1:
    unidades_str = '1 unidade'
    partes_numericas += 1
elif unidades_int > 1:
    unidades_str = f'{unidades_int} unidades'
    partes_numericas += 1

if partes_numericas == 0:
    print('Número 0 não possui centenas, dezenas e nem unidades')
elif partes_numericas == 1:
    print(centenas_str + dezenas_str + unidades_str)
elif partes_numericas == 3:
    print(f'{centenas_str}, {dezenas_str} e {unidades_str}')
elif partes_numericas == 2:
    if centenas_str != '':
        segunda_parte = dezenas_str + unidades_str
        print(f'{centenas_str} e {segunda_parte}')
    else:
        print(f'{dezenas_str} e {unidades_str}')



