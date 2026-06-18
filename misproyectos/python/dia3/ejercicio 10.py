def puede(edad):
    if edad >= 18:
        return "si"
    else:
        return "no"
    
age = int(input("Cuantos años tenes? "))
print(f"Vos {puede(age)} podes votar")