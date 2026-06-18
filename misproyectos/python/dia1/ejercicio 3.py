repetir = True

while repetir == True:

    try:
        numero = int(input(" ¿Dime un numero?: "))
        repetir = False

    except:
        print("Debes ingresar un NUMERO")

Resto = numero%2

if Resto == 0:
    print("El numero es par")
else:
    print("El numero es impar")