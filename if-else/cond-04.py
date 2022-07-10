"""Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, de acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

Si A>=B + C à No se trata de un triángulo

Si A2 = B2 + C2 à Es un triángulo rectángulo

Si A2 > B2 + C2 à Es un triángulo obtusángulo

Si A2 < B2 + C2 à Es un triángulo acutángulo"""

print("Ingrese Lado 1")
lado1 = int(input())
print("Ingrese Lado 2")
lado2 = int(input())
print("Ingrese Lado 3")
lado3 = int(input())

if lado1 >= (lado2 + lado3 ):
    print("No es un triangulo")
elif lado1**2 == (lado2 + (lado3**2)):
    print("Es un triangulo rectangulo")
elif lado1**2 > (lado2 + (lado3**2)):
    print("Es un triangulo obtusangulo")
elif lado1**2 < (lado2 + (lado3**2)):
    print("Es un triangulo acutangulo")