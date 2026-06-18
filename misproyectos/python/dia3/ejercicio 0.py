def celsius(temc):
    temf = temc*9/5+32
    return temf

temp = int(input("Cual es la temperatura hoy en celsius? "))
resultado = celsius(temp)
print(f"{temp}C° son {resultado}F°")


    