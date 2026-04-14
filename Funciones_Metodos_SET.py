# Realizado por Ricardo Camino Lalanda

# FUNCIONES APLICADAS A SET (CONJUNTOS)

# MÉTODOS
print("MÉTODOS (17)\n")

conjunto1 = {1, 2, 3}

# add(): Añade un elemento al conjunto
conjunto1.add(4)
print("- add():")
print(conjunto1)

# remove(): Elimina un elemento del conjunto.
# Si el elemento no existe, genera un error (KeyError)
conjunto1.remove(3)
print("- remove():")
print(conjunto1)

# discard(): Elimina un elemento del conjunto.
# Si el elemento no existe, NO genera error
conjunto1.discard(2)
print("- discard():")
print(conjunto1)

# pop(): Elimina y devuelve un elemento aleatorio del conjunto.
# Si el conjunto está vacío, genera un error
conjunto1.pop()
print("- pop():")
print(conjunto1)

# copy(): Devuelve una copia del conjunto
conjunto2 = conjunto1.copy()
print("- copy():")
print(conjunto1, conjunto2)

# clear(): Elimina todos los elementos del conjunto
conjunto2.clear()
print("- clear():")
print(conjunto2)

conjunto3 = {2, 100}

# union(): Devuelve la unión de dos conjuntos (todos los elementos sin repetir)
print("- union():")
print(conjunto1.union(conjunto3))

# intersection(): Devuelve los elementos comunes entre ambos conjuntos
print("- intersection():")
print(conjunto1.intersection(conjunto3))

# difference(): Devuelve los elementos que están en el primer conjunto
# pero NO en el segundo
print("- difference():")
print(conjunto1.difference(conjunto3))

# symmetric_difference(): Devuelve los elementos que están en uno u otro,
# pero NO en ambos (diferencia simétrica)
print("- symmetric_difference():")
print(conjunto1.symmetric_difference(conjunto3))

# update(): Actualiza el conjunto original agregando los elementos del otro
conjunto1.update(conjunto3)
print("- update():")
print(conjunto1)

# intersection_update(): Actualiza el conjunto original dejando
# solo los elementos comunes
conjunto1.intersection_update(conjunto3)
print("- intersection_update():")
print(conjunto1)

# difference_update(): Actualiza el conjunto original eliminando
# los elementos que también están en el segundo conjunto
conjunto1.difference_update(conjunto3)
print("- difference_update():")
print(conjunto1)

# symmetric_difference_update(): Actualiza el conjunto original
# dejando solo los elementos que no coinciden entre ambos
conjunto1.symmetric_difference_update(conjunto3)
print("- symmetric_difference_update():")
print(conjunto1)

# isdisjoint(): Devuelve True si NO tienen elementos en común (MUY USADO)
print("- isdisjoint():")
print(conjunto1.isdisjoint(conjunto3))

# issubset(): Devuelve True si el conjunto1 está contenido
# completamente dentro de conjunto3
print("- issubset():")
print(conjunto1.issubset(conjunto3))

# issuperset(): Devuelve True si conjunto1 contiene
# completamente a conjunto3
print("- issuperset():")
print(conjunto1.issuperset(conjunto3))