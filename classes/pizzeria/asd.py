variedades = [{'nombre':'napolitana','precio':1200,'ingredientes':{'queso','tomate','salsa','aceituna'}},{'nombre':'mozzarella','precio':1000,'ingredientes':{'queso','salsa','aceituna'}},{'nombre':'especial','precio':1200,'ingredientes':{'queso','tomate','salsa','aceituna','jamon'}}]


for i in variedades:
    print(f"\n{i['nombre'].title()}: ${i['precio']}\nIngredientes: ({','.join([x for x in i['ingredientes']])})")