import pandas as pd 

##ARCHIVO

varchivo=pd.read_csv("D:\programacion\pythonn\python_misTests\goleadores2.csv",index_col="jugador")
print(varchivo)


# Diccionario
# diccionario={
#     "Jugador":["chucky","chicharito","cristiano","messi"],
#     "año":[2016,2016,2016,2016],
#     "goles":[25,85,76,41]
#     }
# print(diccionario)
# jugadores=pd.DataFrame(diccionario)
# print("\n")
# print(jugadores)