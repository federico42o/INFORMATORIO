class Contacto():
    def __init__(self, nombre="", tel=0, email=""):
        self.nombre = nombre
        self.tel = tel
        self.email = email
    def registro(self):
        return f"Nombre: {self.nombre} - Telefono: {self.tel} - Email: {self.email}"

CONTACTOS = []
def agregar_contacto():
    print("AGREGAR CONTACTO")
    nombre = input("Ingrese el nombre: ")
    tel = input("Ingrese el telefono: ")
    email = input("Ingrese el email: ")
    a = Contacto(nombre, tel, email)
    CONTACTOS.append(a)
    return CONTACTOS
d = agregar_contacto()
print(d)