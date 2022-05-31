"""En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 		  PORCENTAJE

Pediatría	   	60%

Traumatología   20%

Kinesiología   	20%


Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado."""


print("Ingrese el presupuesto ANUAL en pesos")
presup = int(input())

ped = ((presup*60)//100)
trau = ((presup*20)//100)
kin = ((presup*20)//100)

print(f"El presupuesto ANUAL sera de ${presup}\n\nPor lo que corresponde\n \nPEDIATRIA \t${ped}\nTRAUMATOLOGIA\t${trau}\nKINESIOLOGIA\t${kin}")