print('Seja-bem vindo À Beira da quadra, qual o seu nome?')
nome = input()

print(f'Que bom ter você aqui {nome}, gostariamos de conhecer um pouco mais você, qual a sua idade?')
idade = input()

print(f'Então, você é {nome} e tem {idade} anos.')
print('E onde você nasceu?')
cidade = input()

print(f'Só para confirmar, você é {nome}, nasceu em {cidade}, tem {idade}, então você nasceu em {2021 - int(idade)}.')
confirmar = input()

print(f'{nome} quer conhecer nossos projetos?')
resposta = input()

print(f'Como sua resposta foi {resposta}, vou te apresentar nossos projetos:')
print(f'A À Beira da quadra foi fundada em 2020 por Henrique Monteiro, e hoje apresente'
      f' lives com diversas pessoas ligadas ao voleibol, desde treinadores, jogadores, comissão'
      f' técninca e outras profissões. Além é claro de realizar transmissões de jogos das diferentes'
      f' categorias. Quer conhecer mais?')
QuerConhecer = input()

print(f'Além das lives e transmissões, Á Beira da Quadra tem parceria com o Arthur Alguma coisa que apresenta'
      f' o quadro tempo ténico e a psicológa Leticia Capuruçu que apresenta um qadro sobre psicologia')
print(f'{nome} você tem alguma dúvida?(Sim ou Não)')
duvidas = input()

if duvidas == 'Sim':
      print('Digite sua dúvida abaixo:')
      duvida = input()
      print(f'Sua dúvida é essa: {duvida}, correto?')
      print('Estamos procurando no sistema a resposta para sua dúvida')
      print(f'Infelizmente não conseguimos responder no momento, para melhor te atender {nome}, '
            f'entre em contado pelo e-mail: abeiradaquadra@gmail.com')
      print('Agradecemos sua participação')
else:
      print(f'{nome}, agradecemos muito a sua presença e até breve!')
