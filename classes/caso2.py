from caso1 import Vehiculo, Coche


class Camioneta(Coche):
    def __init__(self,veloc,cc,carga,color, ruedas):
        super().__init__(veloc,cc, color,ruedas)
        self.carga = carga
    def __str__(self):
        return f"Velocidad maxima: {self.veloc} | Cilindrada: {self.cc}cc. | Carga maxima: {self.carga}Kg. | Color: {self.color} | Cant. de ruedas: {self.ruedas}"

class Bicicleta(Vehiculo):
    def __init__(self,tipo,color,ruedas):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"Tipo de bicicleta: {self.tipo} | Color: {self.color} | Cant. de ruedas: {self.ruedas}"

class Motocicleta(Bicicleta):
    def __init__(self, veloc, cc, color, ruedas,tipo):
        super().__init__(tipo, color, ruedas)
        self.veloc = veloc
        self.cc = cc
    def __str__(self):
        return f"Velocidad maxima: {self.veloc} | Cilindrada: {self.cc}cc. | Color: {self.color} | Cant. de ruedas: {self.ruedas}"

class Catalogar(Vehiculo):
    pass




b = Bicicleta('Urbana', 'Rojo', 2)
cam = Camioneta(250,5000,1000,'Blanco', 4)
m = Motocicleta(150,125,'Azul',2,'Urbana')
c = Coche(244,1600,"Negro",4)
vehiculos = [b, cam, m, c]


def catalogar(lista,ruedas=-1):
    a = ""
    r = 0
    for x in lista:
        a += f"\n{type(x).__name__.center(20)}| {x}\n"
    for i in lista:
        if ruedas == i.ruedas:
            r +=1
    if ruedas != -1:
        a  += f"\nSe han encontrado {r} vehiculos con {ruedas} ruedas"
    return a

if __name__ == '__main__':
    print(catalogar(vehiculos))
    # print(catalogar(vehiculos,0))
    # print(catalogar(vehiculos,2))
    # print(catalogar(vehiculos,4))


