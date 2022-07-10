


# numero = input("Ingrese el nro de telefono con prefijo y extension separado por guiones: ")

# print("El numero de telefono es:",numero[4:-3])

class Futbol():
    def __init__(self,nombre, socios):
        self.nombre = nombre
        self.socios = socios

Futbol.nombre = "Boca Juniors"
Futbol.socios = 298.999

print(f"El club {Futbol.nombre} tiene {Futbol.socios} socios.")


