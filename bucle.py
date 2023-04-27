# bucles


numeros=["0","1","2","3","4","5","6","7","8","9"]
nuevo_numero=""
correo = input("Ingresa una palabra\n")
for numero in correo:
    if  numero in numeros:
     nuevo_numero += numero
print(nuevo_numero)


# i=1 
# while i < 5:
#         print(i)
#         i+=1
# else:
#         print("else:",i)

# numero = 0
# while numero < 10:
#     numero+=1
#     print(numero)
#     if numero == 7:
#         print("llegaste al 7")
#         break

# cadena=input()
# if len(cadena)<=10:
#         print("El mensaje tiene menos de 10 caracteres")
# else:
#         print("La cadena tiene",len(cadena),"caracteres")


# import random
# numero_secreto = random.randint(0,999)
# print("este es mi juego y tienes que adivinar para salir")
# print("que numero estoy pensando")
# while True:
#         numero = int(input("Ingresa el numero"))
#         if numero < numero_secreto:
#           print("Tu numero es pequeño")
#         elif  numero > numero_secreto:
#           print("Tu numero es mayor")
          
#         else:
#           break 
# print("Adivinaste mi numero es", numero)

