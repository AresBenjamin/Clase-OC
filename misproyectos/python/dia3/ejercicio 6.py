def tiempo(mins):
    horas = mins//60
    minsf = mins%60
    return (f"{horas} horas y {minsf} minutos")

minutos = int(input("Dime la cantidad de minutos: "))

print(tiempo(minutos))


