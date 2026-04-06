print(" *** Manejo de listas ***")

mi_lista = [1, 2, 3, 4, 5]
print(f"{mi_lista} -> lista original")

#largo lista
print(f"largo de la lista: {len(mi_lista)}")

#Acceder por indice
print(f"Accedemos al valor almacenado en el indice 4: {mi_lista[4]}")

#ultimo indice de la lista
print(f"Accedemos al ultimo incdice de la lista: {mi_lista[-1]}")

#modificar lista
mi_lista[1] = 10
print(f"Modficamos el valor del indice 1: {mi_lista}")

#agregar elementos a la lista
mi_lista.append(6)
print(f"{mi_lista} -> agregamos el numero 6 a la lista con .append()")

#añadir nuevo elemento en un indice especifico
mi_lista.insert(2, 15)
print(f"{mi_lista} -> se añadio el valor de 15 en el indice 2 con .insert())")

#ELIMIAR ELEMENTOS DE LA LISTA
#metodo remove() -> elimina el primer elemento que coincida con el valor especificado
mi_lista.remove(5)
print(f"{mi_lista} -> se elimino el numero 5 con .remove())")

# Remover por indice con el metodo pop()
mi_lista.pop(1) #elimina el elemento en el indice 1
print(f"{mi_lista} -> se elimino el numero en el indice 1 con .pop()")

#Usando del o delete
del mi_lista[2] #elimina el elemento en el indice 
print(f"{mi_lista} -> se elimino el numero en el indice 2 con del")

#obtener sublistas
sublista = mi_lista[1:3] #obtiene los elementos desde el indice 1 hasta el indice 2 (excluyendo el indice 3)
print(f"{sublista} -> sublista obtenida con slicing [1:3]")
