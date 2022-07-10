"""Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en dispositivos pequeños como teléfonos inteligentes. En este ejercicio, escribirá una función que capitaliza los caracteres apropiados en una cadena. Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y seguida de un espacio. El primer carácter de la cadena también debe estar en mayúscula, así como el primer carácter no espacial después de un ".", "!" o "?" Por ejemplo, si la función se proporciona con la cadena "¿a qué hora tengo que estar allí? ¿cuál es la dirección?" entonces debería devolver la cadena "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?". Incluya un programa principal que lea una cadena del usuario, la capitalice utilizando su función y muestre el resultado."""


def capitalizador(texto):
    new_list = []
    indice = -1
    for letra in texto:
        new_list.append(letra)
    for caracter in new_list:
        indice += 1
        siguiente = indice+1
        if caracter == "¿":
            new_list[siguiente] = new_list[siguiente].upper() 
        elif caracter == "¡":
            new_list[siguiente] = new_list[siguiente].upper()
        elif caracter == ".":
            new_list[siguiente+1] = new_list[siguiente+1].upper()
        elif caracter == "!":
            new_list[siguiente+1] = new_list[siguiente+1].upper()
        elif caracter == "?":
            new_list[siguiente+1] = new_list[siguiente+1].upper()
        elif new_list[0] != "¿" or new_list[0] != "¡":
            new_list[0] = new_list[0].upper()
    return "".join(new_list)


mensaje = input("Ingrese su mensaje: .......")
print(f"\n{capitalizador(mensaje)}")