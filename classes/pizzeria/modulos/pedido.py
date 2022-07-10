import copy
import datetime as dt
from pizza import Pizza
class Pedidos:
    time = dt.datetime.now()
    dt_string = time.strftime("%d/%m/%Y %H:%M:%S")
    TICKET = {
    'Codigo Pedido':0,
    'Fecha y Hora':dt_string,
    'Pago': 'En espera',
    'Demora aprox': ''
    }
    cod_pedido = 0
    def __init__(self,nom_cliente):
        self.pedidos = []
        self.nom_cliente = nom_cliente

    def tomar_pedido(self):
        p = copy.copy(self.TICKET)
        p['Codigo Pedido'] += self.cod_pedido +1
        p['Cliente'] = self.nom_cliente
        return p
        

    def add_pedido(self,*pedido):
        self.cod_pedido +=1
        for a in pedido:
            self.pedidos.append(a)

    def obt_total(self):
        a = 0
        for i in self.pedidos:
            a += i.total()
        return a
    def mostrar_pedido(self):
        print("====================PEDIDO====================")
        
        for a in self.pedidos:        
            print(f"\n{a.comida.nombre.upper()}  x{a.cant} ---------------------- ${float(a.comida.precio)}\n")
            print(f"Tamaño: {a.comida.tamanio}\n")
        
        print(f"TOTAL: ------------------------------ ${float(self.obt_total())}")
        print()
        self.tomar_pedido()
        print(self.TICKET)



class Comanda:

    def __init__(self,comida,cant):
        self.comida = comida
        self.cant = cant
    
    def total(self):
        
        return self.comida.precio*self.cant



if __name__ == '__main__':
    A = Pedidos('Nombre Cliente')
    mozzarella = Pizza('Mozzarella','MO','8P',1100,'M02')
    napolitana = Pizza('Napolitana','PA','8P',1200,'N01')

    C1 = Comanda(mozzarella,4)
    C2 = Comanda(napolitana,7)
    
    A.add_pedido(C1,C2)

    A.mostrar_pedido()


