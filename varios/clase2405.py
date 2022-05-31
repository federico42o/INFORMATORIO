"""Realizar un programa en python, que solicita el ingreso de numeros enteros, teniendo en cuenta lo siguiente:
    - Si se ingresa un valor distinto a un numero entero positivo debera mostrar un mensaje de error y solicitar nuevamente el ingreso de datos.
    - El programa finalizara cuando se ingrese la palabra fin
Al finalizar informar:
    - Cantidad de numeros validos ingresados
    - Cantidad de errores producidos
    - Suma total de todos los numeros ingresados
    - Promedio de numeros ingresados"""

numero = 0 
programa = ""
cantidad_errores = 0
numeros_validos = 0
numeros_ingresados = 0
suma_numeros = 0
promedio = 0

while programa != "fin":
    numero = int(input("Ingrese un numero entero positivo: "))
  
    if numero > 0:
        numeros_validos += 1
    elif numero < 0:
        print("ERROR. Ingrese un numero positivo")
        cantidad_errores +=1

    numeros_ingresados += 1
    suma_numeros += numero
    promedio = suma_numeros//numeros_ingresados
    programa = input("Presione Enter para continuar. Si desea finalizar escriba fin: ")
print(f"""
    - Cantidad de numeros validos ingresados: {numeros_validos}
    - Cantidad de errores producidos: {cantidad_errores}
    - Suma total de todos los numeros ingresados: {suma_numeros}
    - Promedio de numeros ingresados: {promedio}
    """)

