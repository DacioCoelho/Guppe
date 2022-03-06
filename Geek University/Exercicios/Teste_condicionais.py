"""
Teste deu errado
"""

print('Olá, qual o seu nome?')
nome = input()
print(f'{nome}, seja bem vindo! Você gosta de viajar? (Sim  ou Não)')
resposta = input()

if resposta == "Não":
    print("O que você gosta de fazer?")
    hobby = input()
    print(f'Como {hobby} é seu hobby, o que você faz?')
    hobby2 = input()
    print(f'{nome} foi um prazer te conhecer, até uma próxima!')

else:
    print("Para onde você gostaria de viajar?")
    Viagem = input()
    print(f'{nome} o que você gostaria de fazer em {Viagem}?')
    Viagem2 = input()
    print(f'{nome} foi um prazer te conhecer, até uma próxima!')
