"""Nombre, Telefono, Email
1.Añadir contacto
2.Lista de contactos
3.Buscar contacto
4.Editar Contacto
0.Cerrar agenda
"""


class Menu:
    def __init__(self, opciones):
        self.opciones = opciones
    
    def mostrar_menu(self):
        for op in self.opciones:
            print(f"{op['codigo']}: {op['descripcion']}")
        
    def get_opcion(self,opcion):
        for op in self.opciones:
            if op['codigo'] == opcion:
                return op
    
    def opcion_sel(self):
        print('\nElija una opcion')
        sel = int(input(">>"))
        return sel
    
    def start(self):
       while True: 
            
            self.mostrar_menu()
            seleccion = self.opcion_sel()
            sel_dict = self.get_opcion(seleccion)
            getattr(self,sel_dict["funcion"])()
    
    def limpiar_pantalla(self):
        import os
        os.system('cls' if os.name=='nt' else 'clear')
    
    def cerrar(self):
        import sys 
        sys.exit()

menu = [
        {"codigo":1,"descripcion":"Añadir contacto", "funcion": "agregar_contacto"},
        {"codigo":2,"descripcion":"Mostrar contactos", "funcion": "mostrar_contacto"},
        {"codigo":3,"descripcion":"Buscar contacto", "funcion": "buscar_contacto"},
        {"codigo":4,"descripcion":"Editar contacto", "funcion": "editar_contacto"},
        {"codigo":0,"descripcion":"Cerrar agenda", "funcion": "cerrar"},
        

        ]
# m = Menu(menu)

# m.start()

class Contacto():
    def __init__(self,nombre, tel, email):
        
        self.nombre = nombre
        self.tel = tel
        self.email = email
    def registro(self):
        print(f" Nombre: {self.nombre} - Telefono: {self.tel} - Email: {self.email}")



class Agenda(Menu):    
    CONTACTOS = []
    id_c = 0
    def agregar_contacto(self):
        
        print("AGREGAR CONTACTO")
        nombre = input("Ingrese el nombre: ")
        tel = input("Ingrese el telefono: ")
        email = input("Ingrese el email: ")
        self.limpiar_pantalla()
        a = Contacto(nombre, tel, email)
        self.CONTACTOS.append(a)
        
    def mostrar_contacto(self):
        if self.CONTACTOS:
            for a in self.CONTACTOS:
                a.registro()
            input("\nPresione un tecla para continuar")
        else:
            print("Agenda vacia")
        
    
    def buscar_contacto(self):

        print("Ingrese nombre, telefono o email para buscar un contacto")
        b = input()
        self.limpiar_pantalla()
        for e in self.CONTACTOS:
            if b in e.nombre:
                e.registro()
        input("Presione un tecla para continuar")
    
    def editar_contacto(self):
        print("Elija el contacto a editar: ")
        self.mostrar_contacto()
        contact_edit = input(">>")
        for a in self.CONTACTOS:
            a.registro()
        self.limpiar_pantalla()
        if contact_edit in self.CONTACTOS:
            nombre = input("Ingrese el nombre: ")
            setattr(object, 'Nombre', nombre)
            tel = input("Ingrese el telefono: ")
            setattr(object, 'Telefono', tel)
            email = input("Ingrese el email: ")
            setattr(object, 'Email', email)




s = Agenda(menu)
s.start()
