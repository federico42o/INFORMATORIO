from caso1 import Vehiculo, Coche

class Bicicleta(Vehiculo):
    def __init__(self,tipo,color,ruedas):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"Tipo de bicicleta: {self.tipo} | Color: {self.color} | Cant. de ruedas: {self.ruedas} "
    def Caracteristicas(self):
        ca = {"Tipo de bicicleta": self.tipo, "Color":self.color,"Cant. de ruedas":self.ruedas}
        return ca


class Camioneta(Vehiculo):
    def __init__(self,carga, color, ruedas):
        super().__init__(color, ruedas)
        self.carga = carga
    def __str__(self):
        return f"Carga maxima: {self.carga}Kg. | Color: {self.color} | Cant. de ruedas: {self.ruedas}"

class Motocicleta(Coche):
    def __init__(self, veloc, cc, color, ruedas):
        super().__init__(veloc, cc, color, ruedas)
    def __str__(self):
        return f"Velocidad maxima: {self.veloc} | Cilindrada: {self.cc}cc. | Color: {self.color} | Cant. de ruedas: {self.ruedas}"


b = Bicicleta('Urbana', 'Rojo', 2)
cam = Camioneta(1000, 'Blanco', 4)
m = Motocicleta(150,125,'Azul',2)
c = Coche(244,1600,"Negro",4)
bici= b.Caracteristicas()
vehiculos = [bici, cam, m, c]
print(bici["Tipo de bicicleta"])
if bici["Cant. de ruedas"] in (0,2,4):
    print(bici["Cant. de ruedas"])


# def catalogar(lista,ruedas=-1):
#     a = ""
#     r = 0
#     for x in lista:
#         a += f"\n{type(x).__name__} | {x}\n"
#     for i in lista:
#         if ruedas == i.ruedas:
#             r +=1
#     if ruedas != -1:
#         a  += f"\nSe han encontrado {r} vehiculos con {ruedas} ruedas"
#     return a

# if __name__ == '__main__':
#     print(catalogar(vehiculos))
#     print(catalogar(vehiculos,0))
#     print(catalogar(vehiculos,2))
#     print(catalogar(vehiculos,4))


