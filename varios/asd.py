try:
    number = input("Escriba un numero")
    print(f"number * 2 = {number*2+0}" )
except Exception as x:
    
    error = type(x).__name__
    print(f"Ha ocurrido un {error}! Ingrese bien el numero")