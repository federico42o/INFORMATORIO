
class Ingredientes:
    def __init__(self, nombre):
        self.nombre = nombre
    
class Pizza:
    TIPO_PIZZA = {
        'PA':'parrilla',
        'PI':'piedra',
        'MO':'molde'
    } 
    TAMANIO_PIZZA = {
        '8P':'8 porciones',
        '10P':'10 porciones',
        '12P':'12 porciones',
    }  
    def __init__(self,nombre, tipo,tamanio,precio,cod_pizza=''):
        self.nombre = nombre
        self.tipo = tipo
        self.ingred = []
        self.tamanio = tamanio
        self.precio = precio
        self.cod_pizza = cod_pizza
    def add_ingred(self,*ingredientes):
        for i in ingredientes:
            self.ingred.append(i)
    
    def mostrar_ingred(self):
        return ",".join([x.nombre for x in self.ingred])

    def tipo_p(self):
        
        for k, v in self.TIPO_PIZZA.items():
            if self.tipo == k:
                print("Tipo:",v)
    
    
    def demora(self):
        
        d = 0
        
        if self.tipo == 'PA':
            d += 30
        elif self.tipo == 'PI':
            d += 18
        elif self.tipo == 'MO':
            d += 20
        return d


class Menu:
    def __init__(self):
        self.cat = []   

    def agregar_comidas(self,*variedades):
        for c in variedades:
            self.cat.append(c)
    
    def mostrar_menu(self):
        for c in self.cat:
            print(f"\n{c.nombre} ------- ${c.precio}\n")
            print(f"({c.mostrar_ingred()})")
            print("--------------------------------------")




if __name__ == '__main__':
    p = Pizza('Mozzarella','MO','8P',1100,'M02')
    p.demora()
    m = Menu()
    print(m.cat)