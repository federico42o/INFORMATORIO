"""En este ejercicio escribirá una función llamada es_entero que determina si los caracteres en una cadena representan un número entero válido. Al determinar si un string representa un número entero, debe ignorar cualquier espacio en blanco inicial o final. Una vez que se ignora este espacio en blanco, una cadena representa un número entero si su longitud es al menos 1 y solo contiene dígitos, o si su primer carácter es + o - y el primer carácter va seguido de uno o más caracteres, todos los cuales son dígitos Escriba un programa principal que lea una cadena del usuario e informe si representa o no un número entero.

"""


def es_entero(string):
    cadena_limpia = string.strip()
    if cadena_limpia[0] in ("+","-"):
        a = ""
        for x in range(1,len(cadena_limpia)):
           a += cadena_limpia[x]
        return len(a)>=1 and a.isdigit()
    else:
        return len(cadena_limpia)>=1 and cadena_limpia.isdigit()

 
cadena_user = input("ingrese algo.... ")

if es_entero(cadena_user): print(f"{cadena_user} es un entero.")
else: print(f"{cadena_user} NO es un entero")

