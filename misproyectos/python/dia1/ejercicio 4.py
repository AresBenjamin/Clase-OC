repetir = True
while repetir == True:
    try:
        Cant = int(input(" ¿Cuantos dolares queres convertir?: "))
        repetir = False
    except ValueError:
        print("Error,escriba solo NUMEROS")

Pesos = Cant*1000

print (f"Son {Pesos} pesos")