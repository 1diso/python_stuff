#definir la funcion primero antes de mandarla a llamar
#variable tiene preferencia sobre las funciones

# def año_bisiesto(año):
#     if año % 4 == 0:
#         print("Tu año es bisiesto")
#         return False
#     elif año % 100 == 0:
#         return True
#     elif año % 400 == 0:
#         return False
#     else:
#         print("Tu año no es bisiesto")
#         return True

# año=int(input("Ingresa un año\n"))
# año_bisiesto(año)

# def message(): #palabra reservad def, nombre y :
#     print("Esto es una funcion")
# message()
#no se puede revolver palabra clave



# arena=[1,2,3,4,5,6,7,8,9,10]
# buscar=5
# for i in range(len(arena)):
#     encontrar = arena[i] == buscar
#     if encontrar:
#         break
    
# if encontrar:
#     print("encontrado en:", i)
# else:
#     print("no encontrado")

# bronco=["lupe","choche","jose","ramiro"]#lupe,choche,jose luis, ramiro
# print(bronco)
# bronco.append("pelon") #agregar un objeto hasta el final
# print(bronco)   #entra el eplon
# bronco.remove("choche")
# bronco.remove("jose")
# bronco.remove("pelon")
# bronco.remove("ramiro")
# print(bronco) #se disuelva queda lupe
# bronco.append("ramiro")
# print(bronco)#lupe,ramirow 
# bronco.insert(1,"hugo")
# bronco.append("paco")
# bronco.append("luis")#entran hijos hugo, pago, luis
# print(bronco)#bronco

# # for i in reversed(Lista):
# #     print(i,sep="  ",end=" ")

# # print("\n",Lista)

# global peso,altura,imc2


def imc(peso,altura):
    imc2=(peso/(altura**2))
    return imc2
peso=float(input("ingresa tu peso\n"))
altura=float(input("ingresa tu altura\n"))
print("Tu IMC es",imc(peso,altura))
