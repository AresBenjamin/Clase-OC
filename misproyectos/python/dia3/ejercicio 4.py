def mayor(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
    
num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))
num3 = int(input("Dime el tercer numero: "))

rslt = mayor(num1,num2,num3)

print(f"El mayor es: {rslt}")