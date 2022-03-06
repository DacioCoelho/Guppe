class Quadrado:
    def __init__(self, lado=1):
        self.lado = lado

    def mudar_valor_lado(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def retornar_valor_lado(self):
        self.retornar_valor_lado = self

    def calcular_area(self):
        return self.lado ** 2

quadrado = Quadrado()
print(quadrado.lado, quadrado.calcular_area())

quadrado = Quadrado(6)
print(quadrado.lado, quadrado.calcular_area())