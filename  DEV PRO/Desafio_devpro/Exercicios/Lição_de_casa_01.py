"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
 quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
  6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
  em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de
folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math

area_a_ser_pintada = int(input('Qual o tamanho a ser pintado?'))

area_de_folga = area_a_ser_pintada * 1.1


litro_usados = area_de_folga / 6

litros_por_lata = 18
numero_de_latas = math.ceil(litro_usados / litros_por_lata)
valor_lata = numero_de_latas * 80

litros_por_galao = 3.6
numero_de_galao = math.ceil(litro_usados/litros_por_galao)
valor_galao = numero_de_galao * 25

print(f'Você deverá usar {numero_de_latas} latas de tintas, no valor de R${valor_lata},00 ')  #math.ceil  é utilizado para arredondar para cima

print(f'Você deverá usar {numero_de_galao} galões de tintas, no valor de R${valor_galao},00 ')

# Otimizar pelo valor
numero_de_latas = math.floor(litro_usados / litros_por_lata)  #math.floor é o piso (arredonda pra baixo)
valor_lata = numero_de_latas * 80

resto = litro_usados % litros_por_lata
print(resto)

numero_de_galao_resto = math.ceil(resto/litros_por_galao)
valor_galao2 = numero_de_galao_resto * 25

valor_total = valor_lata + valor_galao2
print(valor_galao2)

print(f'Você deverá usar {numero_de_latas} latas e {numero_de_galao_resto} galões, no valor da lata '
      f'de R${valor_lata},00 e valor do galão de R${valor_galao2},00, num total de R${valor_total},00')