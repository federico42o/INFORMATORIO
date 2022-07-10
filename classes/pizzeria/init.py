from modulos.pedido import *
from modulos.pizza import *
from modulos.recepcion import *
# --------------------------------------------------INGREDIENTES--------------------------------------------------
queso_mozzarella = Ingredientes('Mozzarella')
aceituna = Ingredientes('Aceituna')
morron = Ingredientes('Morrón')
cebolla = Ingredientes('Cebolla')
tomate = Ingredientes('Tomate')
salsa = Ingredientes('Salsa')
jamon = Ingredientes('Jamon')
# --------------------------------------------------TIPOS-DE-PIZZA--------------------------------------------------

napolitana = Pizza('Napolitana','PA','8P',1200,'N01')
napolitana.add_ingred(salsa,queso_mozzarella,aceituna,morron,jamon)
# ------------------------------------------------------
mozzarella = Pizza('Mozzarella','MO','8P',1100,'M02')
mozzarella.add_ingred(salsa,queso_mozzarella,aceituna)
# ------------------------------------------------------


# --------------------------------------------------MENU--------------------------------------------------
m = Menu()

m.agregar_comidas(mozzarella,napolitana) #AGREGAMOS LOS TIPOS DE PIZZA AL MENU

p = Pedidos()
