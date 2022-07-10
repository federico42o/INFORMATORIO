class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f"Color: {self.color},Cant. de ruedas: {self.ruedas}"

class Coche(Vehiculo):
    def __init__(self,veloc,cc, color, ruedas):
        super().__init__(color, ruedas)
        self.veloc = veloc
        self.cc = cc
    def __str__(self):
        return f"Velocidad maxima: {self.veloc} Km/h | Cilindrada: {self.cc}cc. | Color: {self.color} | Cant. de ruedas: {self.ruedas}"


c = Coche(244,1600,"negro",4)




if __name__ == '__main__':
    
    print(f"\nTipo: {type(c).__name__}")
    print(f"\nColor: {c.color}")
    print(f"\nCantidad de Ruedas: {c.ruedas}")
    print(f"\nVelocidad Maxima: {c.veloc}Km/h.")
    print(f"\nCilindrada: {c.cc}cc.")