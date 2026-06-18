anioActual = int(2026)

repetir = True

while repetir == True:
    try:
        anioBorn = int(input(" ¿En que año naciste?: "))
        repetir = False
    except ValueError:
        print("Ingresa un numero")


Edad = anioActual-anioBorn

if Edad > 18:
    print("Sos mayor, podes pasar")
else:
    print("Sos menor, no podes pasar")
