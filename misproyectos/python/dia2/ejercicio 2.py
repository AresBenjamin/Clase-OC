notas = [8,9,7,10,6]

nota = 0
suma = 0
vueltas = 0

for nota in notas:
    suma = nota+suma
    vueltas = vueltas+1


promedio = suma/vueltas
print(f"Tu promedio es {promedio}")


