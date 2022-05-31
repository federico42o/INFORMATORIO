from random import randint, choice
maquina = ["La maquina maquiavelica del mal", "Messi", "El bicho"]
continuar = "si"
print("""Instrucciones para jugar: 
- Se puede jugar contra la máquina o contra otro jugador, en cuyo caso ambos serán pateadores.
- El arco se divide en 4 zonas:
    1 = Ángulo superior izquierdo.
    2 = Ángulo inferior izquierdo.
    3 = Ángulo superior derecho.
    4 = Ángulo inferior derecho.
     _____________________
    |  1               3  |
    |       ლ(ಠ_ಠლ)     |
    |           |         |
    |           /\        |  
    |  2               4  |
Se preguntará en cada turno dónde desea patear.""")

while continuar.lower() == "si":
    maquina = choice(maquina)
    goles1 = 0
    goles2 = 0
    rival = input(f"Ingrese 1 para jugar contra un amigo o ingrese 2 para jugar contra {maquina}: ")
    cantpen = int(input("Ingrese la cantidad de penales a patear (Maximo 5): "))
    while cantpen > 5:
        cantpen = int(input("Ingrese la cantidad de penales a patear (Maximo 5): "))
    while rival != "1" and rival != "2":
        rival = input("Opcion no valida, ingrese 1 o 2 (boludo)")
    if rival == "1":
        nombre1 = input("Ingrese nombre de jugador 1: ")
        nombre2 = input("Ingrese nombre de jugador 2: ")
        for i in range(int(cantpen)):
            penal1 = input(f"{nombre1}: Ingrese la dirección del penal utilizando los números del 1 al 4: ")
            atajar1 = randint(1,4)
            print(f"El arquero fue a zona {atajar1}")
            if int(penal1) == atajar1:
                print("Te atajaron")
            else:
                goles1 += 1
                print("GOLAAAAZOOOOOOOO!!")
            penal2 = input(f"{nombre2}: Ingrese la dirección del penal utilizando los números del 1 al 4: ")
            atajar2 = randint(1,4)
            print(f"El arquero fue a zona {atajar2}")
            if int(penal2) == atajar2:
                print("Te atajaron")
            else:
                goles2 += 1
                print("GOLAAAAZOOOOOOOO!!")
    elif rival == "2":
        nombre1 = input("Ingrese nombre de jugador 1: ")
        nombre2 = maquina
        for i in range(5):
            penal1 = input(f"{nombre1}: Ingrese la dirección del penal utilizando los números del 1 al 4: ")
            atajar1 = randint(1,4)
            print(f"El arquero fue a zona {atajar1}")
            if int(penal1) == atajar1:
                print("Te atajaron")
            else:
                goles1 += 1
                print("GOLAAAAZOOOOOOOO!!")
            penal2 = randint(1,4)
            print(f"La computadora decidio patear a la zona {penal2}")
            atajar2 = randint(1,4)
            print(f"El arquero fue a zona {atajar2}")
            if int(penal2) == atajar2:
                print("Penal atajado!!")
            else:
                goles2 += 1
                print("GOLAAAAZOOOOOOOO!!")
    if goles1 > goles2:
        print(f"Ganó {nombre1} {goles1} a {goles2}!!")
    elif goles2 > goles1:
        print(f"Ganó {nombre2} {goles2} a {goles1}!!")
    else:
        print("Empataron los muertos xD.")
    continuar = input("Sale revancha? si / no: ")
