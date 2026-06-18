Num1 = int(input(" Decime el dividendo: "))
Num2 = int(input(" Decime el divisor: "))

if Num2 <= 0:
    print("Error: no se puede dividir por cero")
else:
    div = Num1/Num2
    print(f"El resultado de la division es {div}")