
repetir = True

repeat = True

saldo = 1500

def verpin(pin):
    if pin == 1234:
        return True
    else:
        return False

def retirar(monto):
    if monto > 0:
        if monto <= saldo:
            sacada = saldo-monto
            final = saldo-sacada
            return final
        else:
            return -1
    else:
        return 9999

     

for i in range(4):

    if i < 3:
        while repetir == True:

            try:
                pins = int(input("Ingrese el pin: "))
                repetir = False

            except ValueError:
                print("Debe de ingresar unicamente NUMEROS")

        pinf = verpin(pins)

        if pinf == True:

            while repeat == True:

                try:
                    platasacar = int(input("Ingrese el monto a retirar: "))
                    repeat = False

                except ValueError:
                    print("Debe de ingresar un monto en NUMEROS")

    
            if retirar(platasacar) > saldo:
                print("Error, no se pueden ingresar montos negativos")
                i = 3

            elif retirar(platasacar) > 0:
                print(f"retiraste exitosamente {retirar(platasacar)} pesos")
                i = 3
            else:
                print("Saldo insuficiente")
                i = 3

        else:
            print("PIN incorrecto")
            repetir = True

    else:
        print("Te quedaste sin intentos")

