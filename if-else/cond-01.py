"""Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor."""


list = []
for x in range(3):
    num = int(input("Ingrese un numero: "))
    list.append(num)
print("De mayor a menor:",sorted(list, reverse=True))
   

