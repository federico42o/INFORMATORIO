"""Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de la terminal en caracteres como segundo parámetro. Su función debe devolver una nueva cadena que consta de la cadena original y el número correcto de espacios iniciales para que la cadena original aparezca centrada dentro del ancho proporcionado cuando se imprima. No agregue ningún carácter al final de la cadena. Incluya un programa principal que use su función.
"""
import os
columnas, filas = os.get_terminal_size()
# print(columnas)
# print(filas)

def center(cadena, terminal):

    valor =(terminal-len(cadena))//2
    for e in range(valor):
        cadena = " "+ cadena
    return cadena
# terminal = columnas
terminal = 0
cadena = input("Ingrese una palabra: ")
# while terminal < len(cadena):
#     terminal = int(input("ingrese el tamaño de la terminal: "))
print(center(cadena,terminal))

# print(cadena.center(60))