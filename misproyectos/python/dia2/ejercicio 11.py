import random

adivinado = False

secreto = int(random.randint(0, 100))

print("Pense un numero")

numero = int(input("Dime cual crees que es el numero: "))

while adivinado == False:
    
    if numero > secreto:
        print("incorrecto, el numero es menor")
        numero = int(input("intenta denuevo: "))
        
    elif numero==secreto:
        print ("Correcto, ¡Ganaste!") 
        adivinado = True

    else: 
        print("incorrecto, el numero es mayor")
        numero = int(input("intenta denuevo: "))

   
