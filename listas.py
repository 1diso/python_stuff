#listas
my_list=['python',53,False]

print(type(my_list))#tipo

print(my_list) #lista completa
print(my_list[0]) #posicion 
print(my_list[-2])# -1 imprime la ultima y va en orden descendente#

my_list.append("17") #agregar un objeto hasta el final
print(my_list)

my_list.insert(2,1) #agregar en una psosicion (posicion , obj)
print(my_list)

my_list.remove('python') #Remover el objeto tal cual esta
print(my_list)

my_list.pop(0) #remover posicion de la lista
print( my_list)