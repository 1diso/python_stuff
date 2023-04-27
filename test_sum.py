arena=[1,2,3,4,5,6,7,8,9,10]
buscar=5
for i in range(len(arena)):
    encontrar = arena[i] == buscar
    if encontrar:
        break
    
if encontrar:
    print("encontrado en:", i)
else:
    print("no encontrado")

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



