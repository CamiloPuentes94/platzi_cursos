# Los sirven o se utilizan bastante para hacer join o inner join para las bases de datos

my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set_union = my_set1 | my_set2 # con este operador podemos unir dos sets
print(my_set_union)

my_set_intersectacion = my_set1 & my_set2 # con este operador podemos intersectar dos sets
print(my_set_intersectacion)

# Se ejecuta la diferencia entre los sets
my_set_diferencia1 = my_set1 - my_set2
print(my_set_diferencia1)

my_set_diferencia2 = my_set2 - my_set1
print(my_set_diferencia2)

# diferencia simetrica -- se queda con los valores que no se comparten los sets
my_set_diff_simetrica = my_set1 ^ my_set2
print(my_set_diff_simetrica)