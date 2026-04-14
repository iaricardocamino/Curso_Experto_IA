# Realizado por Ricardo Camino Lalanda

# FUNCIONES APLICADAS A DICT (DICCIONARIOS)

# MÉTODOS
print("MÉTODOS (11)\n")

diccionario1 = {"a": 1, "b": 2, "c": 3}

# get(): Devuelve el valor de una clave.
# Si no existe, devuelve None (o el valor que indiquemos)
print("- get():")
print(diccionario1.get("a"))
print(diccionario1.get("z", "No existe"))

# clear(): Elimina todos los elementos del diccionario
diccionario2 = diccionario1.copy()
diccionario2.clear()
print("- clear():")
print(diccionario2)

# copy(): Devuelve una copia del diccionario
diccionario3 = diccionario1.copy()
print("- copy():")
print(diccionario1, diccionario3)

# keys(): Devuelve todas las claves del diccionario
print("- keys():")
print(diccionario1.keys())

# values(): Devuelve todos los valores del diccionario
print("- values():")
print(diccionario1.values())

# items(): Devuelve clave y valor en forma de tuplas
print("- items():")
print(diccionario1.items())

# pop(): Elimina la clave indicada y devuelve su valor.
# Si no existe, genera error (salvo que indiquemos valor por defecto)
diccionario4 = diccionario1.copy()
diccionario4.pop("c")
print("- pop():")
print(diccionario4)

# popitem(): Elimina y devuelve el último par clave-valor insertado
diccionario5 = diccionario1.copy()
diccionario5.popitem()
print("- popitem():")
print(diccionario5)

# fromkeys(): Crea un nuevo diccionario con las claves indicadas
# y un valor común para todas
print("- fromkeys():")
nuevo_diccionario = dict.fromkeys(["x", "y", "z"], 0)
print(nuevo_diccionario)

# setdefault(): Devuelve el valor de la clave.
# Si no existe, la crea con el valor indicado
diccionario6 = diccionario1.copy()
diccionario6.setdefault("z", 100)
print("- setdefault():")
print(diccionario6)

# update(): Actualiza el diccionario agregando o modificando elementos
diccionario7 = diccionario1.copy()
diccionario7.update({"d": 4, "a": 99})
print("- update():")
print(diccionario7)