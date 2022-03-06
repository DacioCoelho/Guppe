
lista = []
for _ in range(10):
    numero = float(input('Digite um número: '))
    lista.append(numero)
    lista.sort()       #Organizar em forma crescente
print(lista)
lista.reverse()
print(lista)
