repetir = True
while repetir == True:
    
    try:
        Cuenta = float(input(" ¿Cuanto es la cuenta?: "))
        repetir=False

    except ValueError:
        print("Solo puede ingresar numeros")

manteca= True

while manteca == True:
    try:
        Porcentaje = int(input("¿Cual es el porcentaje?: "))
        manteca=False

    except ValueError:
        print("Solo puede ingresar numeros")


Prop = (Cuenta*Porcentaje)/100

Monto = Cuenta+Prop

print(f"Tu propina es: {Prop}")

print(f"Tu monto es: {Monto}")
