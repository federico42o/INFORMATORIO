"""CASO 3
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno)."""


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def tipo_triangulo(self):
        x = {1:"Triangulo Equilatero",2:"Triangulo Isoceles",3: "Triangulo Escaleno" }
        return x[len({self.lado1,self.lado2,self.lado3})]
    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

print("A continuacion le pediremos los 3 lados de un triangulo")
try:
    a,b,c = [int(x) for x in input("Ingrese las longitudes de los 3 lados, separados por un espacio: ").split()]
    t = Triangulo(a,b,c)

    print(f"Es un {t.tipo_triangulo()}")

    print(f"El lado mayor del triangulo mide: {t.lado_mayor()}")

except:
    print("Solo se admiten 3 lados, separados por un espacio.")

# t = Triangulo(a,b,c)

# print(f"Es un {t.tipo_triangulo()}")

# print(f"El lado mayor del triangulo mide: {t.lado_mayor()}")