telef ={
    "Benjamin":"11 2345 6787",
    "Santiago":"11 3245 5545",
    "Santino":"11 3444 6655",
}
nombre = input("Ingresa un nombre ")
print(f"El numero de telefono es {telef.get(nombre,"No encontrado")}")