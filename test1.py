# print('oal amigos')

# print(1+3)

# print("Programming","Essentials","in",sep="***", end="...")
# print("Python")
# #Muestra: Programming***Essentials***in...Python

# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")


# print("    *","\n   * *","\n  *   *","\n *     *","\n***   ***","\n  *   *","\n  *   *","\n  *   *","\n  *****")

# print("    *","        *")
# print("   * *","      * *")
# print("  *   *","    *   *")
# print(" *     *","  *     *")
# print("***   ***","***   ***")
# print("  *   *","    *   *")
# print("  *   *","    *   *")
# print("  *****","    *****")

# print("    *    "*2)
# print("   * *   "*2)
# print("  *   *  "*2)
# print(" *     * "*2)
# print("***   ***"*2)
# print("  *   *  "*2)
# print("  *   *  "*2)
# print("  *****  "*2)


import math


my_list=["    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *   *","  *****"]
n=len(my_list)
for i in reversed(my_list):
        print(i)
        
for i in my_list:
    print(i)
        

# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])
# print(my_list[-5])
# print(my_list[-6])
# print(my_list[-7])
# print(my_list[-8])
# print(my_list[0])


# a = 2
# b = 3
# resultado = a + b
# print(resultado)

# print(0o127)
# nombre = input()

# print("Hola" ,nombre,"bienvenido a un nuevo tutorial")


numero_1=float(input("ingrese el primer numero\n"))
numero_2=float(input("ingrese el segundo numero\n"))

resultado=math.sqrt(numero_1**2+numero_2**2)
print("El resultado es:",resultado)

