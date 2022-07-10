import time
# Desafío 1
# 150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

# Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

# Un trozo de chicle tarda 5 años en degradarse. 

# Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.

def info(elemento):
    tipo = "Tipo no valido"
    degradacion= "-"
    if elemento == "1":
        tipo = "Bolsa de plástico"
        degradacion= "150 años"
    elif elemento == "2":
        tipo = "Botella PET"
        degradacion= "1000 años"
    elif elemento == "3":
        tipo = "Envase tetrabrik"
        degradacion= "30 años"
    elif elemento == "4":
        tipo = "Chicle"
        degradacion= "5 años"

    return tipo, degradacion


print("""
        Por favor, seleccione el tipo de elemento ingresando el numero correspondiente.

        1-Bolsa de plástico
        2-Botella PET
        3-Envase tetrabrik
        4-Chicle

""")
elemento = input()
info
info_elemento = info(elemento)
# tipo, elemento = info(elemento) # Tambien funciona

print(f"Tipo: {info_elemento[0]}\nTiempo de degradacion: {info_elemento[1]}.")






