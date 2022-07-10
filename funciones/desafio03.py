"""Desafío 3
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena."""

from random import randint
ciudades = [["Buenos Aires"],["Rosario"],["Cordoba"],["Rosario"],["Salta"],["Corrientes"],["Resistencia"],["Posadas"],["Parana"],["Formosa"]]
def lista_random(lista):
    for x in range(10):
        nums = randint(5,160)
        ciudades[x].append(nums)
    return lista


datos_ciudades=lista_random(ciudades)
def separar(lista_arboles):
    supera = []
    no_supera = []
    arboles_bien = 0
    for x in range(0,len(lista_arboles)):
        if lista_arboles[x][1] >= 100:
            supera.append(lista_arboles[x])
            supera.sort()
            arboles_bien += 1
        else:
            no_supera.append(lista_arboles[x])

    return supera, no_supera,arboles_bien



resultado=(separar(ciudades))

print(f"\nHubo {resultado[2]} ciudades que plantaron mas de 100: {resultado[0]}\n\nCiudades que no: {resultado[1]}")
