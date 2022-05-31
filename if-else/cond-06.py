"""Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: Número de pulsaciones = (220 - edad)/10"""

print("Ingrese su edad")
edad = int(input())
pulsaciones = (220 - edad)/10
print(f"Con {edad} años sus pulsaciones cada 10 segundos deberian ser de {pulsaciones}")