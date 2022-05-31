"""Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:

Sueldo Actual (en $)    Aumento

0 – 6000							15%

6000 – 7900					   10%

7900 – 12000					6%

Más de 12000				   0%

Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado."""

print("Ingrese sueldo del jugador: ")
sueldo = int(input())

if sueldo <= 12000 and sueldo >= 7900:
    aumento =  (sueldo * 6)/100
    print(f"A su sueldo de ${sueldo} le corresponde un aumento del 6% y ahora cobrará {aumento+sueldo}")
elif sueldo >=6000 and sueldo <= 7900:
    aumento = (sueldo * 10)/100
    print(f"A su sueldo de ${sueldo} le corresponde un aumento del 10% y ahora cobrará {aumento+sueldo}")
elif sueldo <= 6000 and sueldo >= 0:
    aumento = (sueldo * 15)/100
    print(f"A su sueldo de ${sueldo} le corresponde un aumento del 15% y ahora cobrará {aumento+sueldo}")
else:
    print(f"A su sueldo de ${sueldo} no le corresponde ningun aumento")