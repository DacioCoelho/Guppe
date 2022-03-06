"""print('Hello Mundo')

print('Quantos anos você tem?')
numero = input()
print(f'Você tem {numero} anos')

print('Quantos reais você tem?')
reais = int(input())
print('Quanto você tinha?')
total = int(input())
gasto = total - reais
print(f'Você tinha {total} reais e gastou {gasto} reais')
"""


"""
nota1 = float(input('Nota da 1ª prova:'))
nota2 = float(input('Nota da 2ª prova:'))
nota3 = float(input('Nota da 3ª prova:'))
nota4 = float(input('Nota da 4ª prova:'))

media = (nota1 + nota4 + nota3 + nota2)/4

print(f'A sua média nas provas foi: {media}')
"""

salario_por_hora = float(input('Quanto você ganha por hora?'))
horas_trabalhadas =float(input('Quantas horas você trabalha por mês?'))

salario_bruto = salario_por_hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f'Você recebe de salário bruto, o valor de {round(salario_bruto)} reais.'
      f'Os descontos em folha são {round(ir)} reais de imposto de renda, {round(inss)} reais '
      f'de INSS e {round(sindicato)} reais para o sindicato, dando um total de {round(descontos)} reais.'
      f'Recebendo de salário líquido o valor de {round(salario_liquido)} reais.')

print(f"""+ Salário Bruto : R$ {round(salario_bruto)}
- IR (11%) : R$ {round(ir)}
- INSS (8%) : R$ {round(inss)}
- Sindicato ( 5%) : R$ {round(sindicato)}
= Salário Liquido : R${round(salario_liquido)} """)


"""
Quem_é_voce = input('Boa tarde, gostaria de calcular o seu peso ideal?')

sexo = int(input('Que ótimo, para iniciar digite 1, se você for do sexo masculino'
             'ou digite 2 se você for do sexo feminino:'))

if sexo == 1:
    altura = float(input('Qual sua altura:'))
    peso_ideal = (72.7*altura) - 58
    print(peso_ideal)

else:
    altura = float(input('Qual sua altura'))
    peso_ideal = (62.1*altura) - 44.7
    print(f' O seu peso ideal é {round(peso_ideal)} quilos')
"""

"""
Quem_e_você = input('Seja-bem vindo ao Espaço Pro, qual o seu nome?')

sexo = input(f'Olá {Quem_e_você}, para te conhecer melhor, digite M se você for do sexo masculino e F, se você'
             f'for do sexo feminino:')

sexo = sexo.upper()

if sexo == 'M':
    print(input('Você é do sexo masculino então, correto?'))
elif sexo == 'F':
    print(input('Você é do sexo feminino então, correto?'))
else:
    print('Sua resposta não está definida')
    
    """
