print(" *** Promedio de calificaciones *** ")

#lista vacia
calificaciones = []
numero_calificaciones = int(input("Proporciona el no. de calificaciones a evaluar: "))

#iteramos cada elemento para agregar calificaciones a la lista
for indice in range(numero_calificaciones):
    calificacion = float(input(f"Calificacion [{indice}]: "))
    calificaciones.append(calificacion)

#promedio
print()
print(f"Las calificaciones ingresadas son: {calificaciones}")
promedio_calificaciones = sum(calificaciones) / len(calificaciones)
print(f"\nEl promedio de las calificaciones es: {promedio_calificaciones:.2f}")