"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
# 1
"""
while True:
    try:
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
    except ValueError:
        print('Deve ser um número inteiro')
    else:
        if login != senha:
            print('Login concluido!')
            break
        else:
            print('Login e senha precisam ser diferentes.')
"""
"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; """


print('Seja bem vindo ao registro da empresa, todas as informações serão solicitadas e confirmadas,'
      'qualquer dúvida entre em contato no telefone')
while True:
    try:
        nome = input('Digite seu nome: ')
    except TypeError:
        print('Deve ser um nome, sem números')
    else:
        if len(nome) >= 3:
            while True:
                try:
                    Idade = int(input(f'{nome}, quantos anos você tem: '))
                except ValueError:
                    print('Deve ser um número inteiro')
                else:
                    if 1 <= Idade <= 150:
                        while True:
                            try:
                                salario = float(input('Qual seu salário: '))
                            except ValueError:
                                print('Deve ser apresentado o valor sem R$, apenas o valor númerico.')
                            else:
                                if salario > 0:
                                    while True:
                                        try:
                                            sexo = input('Digite M para masculino e F para feminino: ')
                                            sexo = sexo.upper()
                                        except TypeError:
                                            print('Por favor digite novamente, a informação contou com um  erro.')
                                        else:
                                            if sexo == 'F':
                                                while True:
                                                    try:
                                                        estado_civil = input('Qual seu estado civil:'\
                                                                             'Digite 1 para solteiro(a)'\
                                                                             'Digite 2 para casado(a)'\
                                                                             'Digite 3 para viuvo(a)'\
                                                                             'Digite 4 para divorciado(a)')

                                                    except TypeError:
                                                        print('Reveja as informações')
                                                    else:
                                                        if estado_civil == '1':
                                                            print('Você é solteiro.')
                                                            break
                                                        elif estado_civil == '2':
                                                            print('Você é casado.')
                                                            break
                                                        elif estado_civil == '3':
                                                            print('Você é víuvo.')
                                                            break
                                                        elif estado_civil == '4':
                                                            print('Você é divorciado.')
                                                            break
                                                        else:
                                                            print('Digite novamente seu estado civil')
                                                break
                                            elif sexo == 'M':

                                                while True:
                                                    try:
                                                        estado_civil = input('Qual seu estado civil: '
                                                                             'Digite 1 para solteiro(a) '
                                                                             'Digite 2 para casado(a)  '
                                                                             'Digite 3 para viuvo(a)  '
                                                                             'Digite 4 para divorciado(a)    ')

                                                    except TypeError:
                                                        print('Reveja as informações')
                                                    else:
                                                        if estado_civil == '1':
                                                            print(f' Seu cadastro foi completo.'
                                                                  f'Aqui estão as suas informações:'
                                                                  f'Nome = {nome} '
                                                                  f'Idade = {Idade} '
                                                                  f'Salário = R${salario} '
                                                                  f'Estado Civil = {estado_civil} ')
                                                            break
                                                        elif estado_civil == '2':
                                                            print(f' Seu cadastro foi completo.'
                                                                  f'Aqui estão as suas informações:'
                                                                  f'Nome = {nome} '
                                                                  f'Idade = {Idade} '
                                                                  f'Salário = R${salario} '
                                                                  f'Estado Civil = {estado_civil} ')
                                                            break
                                                        elif estado_civil == '3':
                                                            print(f' Seu cadastro foi completo.'
                                                                  f'Aqui estão as suas informações:'
                                                                  f'Nome = {nome} '
                                                                  f'Idade = {Idade} '
                                                                  f'Salário = R${salario} '
                                                                  f'Estado Civil = {estado_civil} ')
                                                            break
                                                        elif estado_civil == '4':
                                                            print(f' Seu cadastro foi completo.'
                                                                  f'Aqui estão as suas informações:'
                                                                  f'Nome = {nome} '
                                                                  f'Idade = {Idade} '
                                                                  f'Salário = R${salario} '
                                                                  f'Estado Civil = {estado_civil} ')
                                                            break
                                                        else:
                                                            print('Digite novamente seu estado civil')
                                                break
                                            else:
                                                print('Por favor digite novamente')
                                    break
                                else:
                                    print('Para o cadastro é necessário ter renda.')
                        break
                    else:
                        print('Não é possivel o registro com essa idade')
            break
        else:
            print('Nome menor do que o exigido.')










