print("Tuplas")

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)

#Tuplas no se pueden modificar, son inmutables
#mi_tupla[0] = 10 # Esto generará un error
#mi_tupla.append(6) # Esto también generará un error

#iteramos los elementos de la tupla
for elemento in mi_tupla:
    print(elemento, end= ' ')

#Crear una tupla de coordenadas

coordenadas = (3, 5)
#Accedemos a cada elemento de la tupla
print()
print("\nCoordenadas:")
print(f"coordenada x: {coordenadas[0]}")
print(f"coordenada y: {coordenadas[1]}")

#tupla unitaria
tupla_unitaria = (10,) # Es importante incluir la coma para que sea reconocida como tupl
print("\nTupla unitaria:")
print(tupla_unitaria)

#tupla anidada
tupla_anidada = (1, (2, 3), (4, 5))