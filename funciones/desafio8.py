"""Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en dispositivos pequeños como teléfonos inteligentes. En este ejercicio, escribirá una función que capitaliza los caracteres apropiados en una cadena. Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y seguida de un espacio. El primer carácter de la cadena también debe estar en mayúscula, así como el primer carácter no espacial después de un ".", "!" o "?" Por ejemplo, si la función se proporciona con la cadena "¿a qué hora tengo que estar allí? ¿cuál es la dirección?" entonces debería devolver la cadena "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?". Incluya un programa principal que lea una cadena del usuario, la capitalice utilizando su función y muestre el resultado."""


#recibo un string, lo divido segun . , ! ? y despues, busco el indice de dicho caracter, le sumo 1, lo capitalizo
# string = "¿a qué . hora tengo !q!ue . esta¡r allí? ¿cuál es la dirección?a ! jajaja ! nos vemos. chauyuu"
def capitalizador(string):
    # string = string.replace("","")
    chars_fin = ["!",".","?"]
    chars_ini = ["¿","¡"]
    nuevo_str = []
    indice = -1
    for letra in string:
        nuevo_str.append(letra)
    
    for caracter in nuevo_str:
        indice += 1
        siguiente = indice+1
        if caracter in chars_fin:
            if nuevo_str[siguiente+1] not in chars_ini:
                nuevo_str[siguiente+1] = nuevo_str[siguiente+1].upper()
            else:
                nuevo_str[siguiente+2] = nuevo_str[siguiente+2].upper()
        elif caracter in chars_ini:
            nuevo_str[siguiente] = nuevo_str[siguiente].upper()
        

    return (nuevo_str)

string = input("escriba su mensaje....")
resultado = "".join(capitalizador(string))
print(resultado)

print()