import matplotlib.pyplot as plt

c1= int(input("Ingresa tu calificacion de matematicas\n"))
c2= int(input("Ingresa tu calificacion de ingles\n"))
c3= int(input("Ingresa tu calificacion de calculo\n"))

data = {"matematicas":c1,"Ingles":c2,"calculo":c3}

materia = list(data.keys())
values = list(data.values())

print(data)
print(materia)
print(values)

fig = plt.figure(figsize=(10,5))
plt.bar(materia,values,color="green",width=0.5)
plt.xlabel("Materias")
plt.ylabel("Calificacion")
plt.title("Calificaciones")
plt.show()
