"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class BolaCirculo:    #Lembre-se de tipo
    def __init__(self):   #Metodo Dander inte (é quando se utiliza __ e depois __)
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'
    def mostra_cor(self):
        return id(self)

    def trocar_cor(self, cor):
        self.cor = cor

circulo_primeiro = BolaCirculo()
circulo_segundo = BolaCirculo()

print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)

print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
print(id(circulo_segundo),circulo_segundo.trocar_cor('Vermelho'))


print(circulo_primeiro.cor, circulo_segundo.cor)
print(circulo_primeiro.circunferencia, circulo_segundo.circunferencia)
circulo_primeiro.circunferencia = 7
print(circulo_primeiro.circunferencia, circulo_segundo.circunferencia)

