precio = int(input("¿Cual es el precio original?"))
descuento = int(input("¿Que porcentaje? "))
cant = (precio*descuento)/100
total = precio - cant
print (f"tu precio es {total}")
print (f"tu descuento es {cant}")
