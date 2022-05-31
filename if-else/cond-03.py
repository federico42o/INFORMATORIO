"""Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos."""

print("Ingrese un numero")
num1= int(input())
print("Ingrese otro numero")
num2= int(input())
print("Ingrese otro numero")
num3= int(input())

if num1 < num2 and num1 < num3:
    print(f"{num1} es menor que {num2} y {num3}")
elif num1 < num2:
    print(f"{num1} es menor que {num2} pero no es menor que {num3}")
elif num1 < num3:
    print(f"{num1} es menor que {num3} pero no es menor que {num2}")
else:
    print(f"{num1} no es menor que ninguno")
