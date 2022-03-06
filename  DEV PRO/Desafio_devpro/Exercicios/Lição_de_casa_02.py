print('Seja bem-vindo ao sistema de notas do CDC!')
nome = input('Para iniciar nosso programa, digite o seu nome:')

print(f'Que bom ter você aqui {nome}.')
print('Para saber se você está aprovado, digite suas duas notas:')
nota1 = float(input('Nota da 1ª etapa:'))
nota2 = float(input('Nota da 2ª etapa:'))

nota_final = (nota1 + nota2)/2

if nota_final == 10:
    print(f'{nome}, você foi APROVADO COM EXCELÊNCIA com a nota {nota_final}.')
elif nota_final < 5.5:
    print(f'{nome}, você foi REPROVADO com a nota {nota_final}.')
elif nota_final > 6:
    print(f'{nome}, você foi APROVADO com a nota {nota_final}.')
else:
    print(f'{nome}, você foi APROVADO COM DEPENDÊNCIA com a nota {nota_final}.')


