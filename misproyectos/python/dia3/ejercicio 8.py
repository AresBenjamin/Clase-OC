def final(precio, descuento):
    precios = (100*descuento)/precio
    preciof = precio - precios

    return preciof

prec = int(input("Dime el precio: "))
desc = int(input("Dime el descuento: "))
print(f"El precio final es {final(prec,desc)}")