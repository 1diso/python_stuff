# SETS

my_set = {}
print(type(my_set))

my_set = {"oal", 17, 1.11, False}
print(my_set)  # Los sets no tienen orden

my_set.add(17)  # No agrega valores duplicados
print(my_set)

my_set.add(17.50)  # Sia grega valores diferentes
print(my_set)

my_set2 = {"oal", 17, 90, False}  # Imprime los datos diferentes de los sets
my_set.difference_update(my_set2)
print(my_set)

my_set2.difference_update(my_set)  # Imprime los datos diferentes de los sets
print(my_set2)
