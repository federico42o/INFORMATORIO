payaso = 112
muñeca = 75

peso_payasos = float(input("Ingrese la cantidad de Payasos: "))
peso_munecas = float(input("Ingrese la cantidad de Muñecas: "))
peso_total = ((peso_payasos * payaso) + (peso_munecas * muñeca))
print ("El peso total de los payasos es de: ", float(peso_payasos * payaso), " gramos")
print ("Y el peso total de las muñecas es de: ", float(peso_munecas * muñeca), " gramos")

print("El peso total del paquete es: ", str(peso_total))