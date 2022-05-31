"""En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento."""

tienda_abierta = "si"
descuento = 0
color: ""

while tienda_abierta == "si":
    compra = int(input("Ingrese el valor de su compra: "))
    tapitas = int(input("Ingrese la cantidad de tapitas: "))
    if tapitas >= 50:
        color= "rojo"
        descuento=40

    elif tapitas>=30:
        color ="amarillo"
        descuento=25
    else:
        color = "blanco"
    
    print(f"Gracias por su donacion, usted obtuvo un cupon de color {color}con un descuento del {descuento}% ")
    tienda_abierta = input("Desea hacer otra donacion?")