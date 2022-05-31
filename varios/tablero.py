CELDA = ""

columnas = int(input("Ingrese el numero de columnas: "))
filas = int(input("Ingrese el numero de filas: "))

for i in range (1,filas+1):
    for j in range(1,columnas+1):
        if (i+j) % 2 ==0:
           print(CELDA+"🟩",end="")
        else:
            print(CELDA+"🔲",end="")
    print("")



















# cuadrados = [x**2 for x in range(1,11)]
# print(cuadrados)
# impares = [x for x in cuadrados if x%2!=0]
# print(impares)