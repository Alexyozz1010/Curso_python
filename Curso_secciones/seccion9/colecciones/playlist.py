print(" *** Playlist de canciones *** ")

#Lista vacia para almacenar las canciones
lista_reproduccion = []

numero_canciones = int(input("¿Cuántas canciones deseas agregar a tu playlist?: "))

#iteramos cada elemento para agregar canciones a la playlist
for indice in range(numero_canciones):
    cancion = input(f"Ingresa el nombre de la canción {indice + 1}: ")
    lista_reproduccion.append(cancion)

#ordenar la playlist en orden alfabetico
#lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort() #orden alfabetico de la A a la Z


#Mostrar la lista iterando sus elementos
print(f"\nLista de reproduccion iterada: ")
for cancion in lista_reproduccion:
    print(f"- {cancion}")