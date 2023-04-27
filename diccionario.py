# diccionario

my_dict = {"nombre": "raul",
           "edad": 20,
           "apellido": "Moreno"}

print(my_dict["nombre"])
print(my_dict["apellido"])
my_dict["apellido"]="Flores"
print(my_dict.keys())
print(my_dict.values())
my_dict.update({"sexo":"masculino"}) #agrego una nueva clave
print(my_dict)
my_dict.popitem() #saca la ultima calve ingresada5470
for key in sorted(my_dict.keys()): #recorrido y ordenamiento alfabetico
    print(key, "->",my_dict[key])
my_dict = list(my_dict) #convierto el diccionario a lista
print(my_dict)
