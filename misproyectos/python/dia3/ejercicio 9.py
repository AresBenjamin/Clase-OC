def email(nombre,apellido):
    j = nombre + "." + apellido + "@empresa.com"
    return j

name=input("Decime un nombre: ")
apell=input("Decime un nombre: ")

print(f"Su email es {email(name,apell)}")
