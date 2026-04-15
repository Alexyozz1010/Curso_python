print("*** Manejo de sets ***")

mi_set = {1, 2, 3, 4, 5, 4}
print(f"Mi set: {mi_set}")

#Agregar elementos a un set
mi_set.add(6)
mi_set.add(7)

#agg elementos duplicados 
mi_set.add(3)
mi_set.add(2)
print(f"Mi set después de agregar un elemento duplicado: {mi_set}")

#Eliminar un elemento del set
mi_set.remove(4)
print(f"Mi set después de eliminar el elemento 2: {mi_set}")

#Iterar loslementos del set
for elemento in mi_set:
    print(elemento, end=' ')

#Comprpbar exixsencia de un elemento en el set
print(f"\nExiste el elemento 4 en el set? {4 in mi_set}")

#Obtener longitud del set con la función len()
print(f"Longitud del set: {len(mi_set)}")