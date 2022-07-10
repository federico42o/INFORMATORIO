"""Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"

Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"

Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"

Tamaño sobredimensionado: Mensaje "Pez contaminado" """

# print("CONTROL DE PECES \n \n")

# print("Ingrese el tamaño del pez: \n >Normal  \n >Debajo de lo normal \n >Encima de lo normal \n >Sobredimensionado")
# tamanio_pez = input().capitalize()

# if tamanio_pez == 'Normal':
#     print("Pez en buenas condiciones ")
# elif tamanio_pez == 'Debajo de lo normal':
#     print("Pez con problemas de nutrición ")
# elif tamanio_pez == 'Encima de lo normal':
#     print("Pez con síntomas de organismo contaminado ")
# elif tamanio_pez == 'Sobredimensionado':
#     print("Pez contaminado ")


from getpass import getpass

password = getpass("Ingresa su contraseña: ")

print(password)