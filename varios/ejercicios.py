numero =""
cantidad_errores = 0
numeros_validos = 0
suma_numeros = 0
while numero != 0 :
    numero = int(input("Ingrese un numero entero positivo: para finalizar escriba fin  " ))
    if numero == 0:
        print("Programa finalizado")
    if numero > 0:
        print("es positivo")
        numeros_validos += 1
        suma_numeros= suma_numeros + numero
    elif numero < 0:
        print("ERROR. Ingrese un numero positivo")
        cantidad_errores +=1
print(f"""
    - Cantidad de numeros validos ingresados{suma_numeros}
    - Cantidad de errores producidos
    - Suma total de todos los numeros ingresados
    - Promedio de numeros ingresados
    """)