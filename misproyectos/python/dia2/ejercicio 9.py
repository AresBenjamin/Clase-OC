precios = {
    "Manzana":100,
    "Pera":50,
    "Uva": 25
}

fruta = input("Dime la fruta: ")
Kilos = int(input("Dime la cantidad de Kg: "))

precio = precios.get(fruta)

total = precio*Kilos

print("El total es: ", total)