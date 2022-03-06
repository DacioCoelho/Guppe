"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade
de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra
 o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível
 total na bomba."""

class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro: float, quantidade_combustivel:float):
        self.valor_litro = valor_litro
        self.tipo_combustivel = tipo_combustivel
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor:float):
        litros_abastecidos = valor / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos

        print(f'Foram Abastecidos {litros_abastecidos:.2f} litros a um valor de R${valor:.2f}')
        print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}')

    def abastecer_por_litros(self, litros:float):
        valor = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos

        print(f'Foram Abastecidos {litros_abastecidos:.2f} litros a um valor de R${valor:.2f}')
        print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}')
bomba = BombaCombustivel('Gasolina', 4.59 , 100.0)

bomba.abastecer_por_valor(100)



