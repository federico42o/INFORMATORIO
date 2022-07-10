from modulos.pedido import *
from init import m,p,mozzarella,napolitana

class Dia(Pedidos):

    # def abrir_caja(self,time):
    #     init_time = dt.datetime.now()







    def start(self):

        print("Bienvenido")
        
        while True:
            print("Nuestro menú disponible: ")
            m.mostrar_menu()
            n_cliente = input("Nombre cliente: \n")
            print("---Agregar pedido----")
            n_pe = input("Pizza: ")
            cant_p = int(input("Cant: "))
            desc = f"{n_pe}    x{cant_p}"
            demora = mozzarella.demora()*cant_p
            p = p.tomar_pedido(n_cliente, desc,demora)
            p.add_pedido(p)
            p.mostrar_pedido()
            print("\nSe ha registrado su pedido exitosamente.")
            # a=input("Desea registrar otro pedido? s/n ")
            # if a == 'n':
            #     break




