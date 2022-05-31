"""Desarrolle un programa que permita determinar si un número X ingresado es par o impar."""
count = 0
while count < 1:
    print("ingrese cualquier numero")
    num_x = int(input())
    count +=1
    if num_x % 2 == 0:
        print(f"{num_x} es par.")
    else:
        print(f"{num_x} es impar.")