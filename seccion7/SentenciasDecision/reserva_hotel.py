print("*** Sistema de Reserva de Hotel ***")

tarifa_diaria_sin_vista = 100.50
tarifa_diaria_con_vista = 150.50

nombre_cliente = input("Ingrese su nombre: ")
dias_estadia = int(input("Ingrese el número de días de su estadía: "))
vista_al_mar_txt = input("Con vista al mar (Si/No)?")
vista_al_mar = vista_al_mar_txt.strip().lower() == "si"

if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista

print("\n----------------- Detalles de la Reserva -------------------")
print(f"Nombre del cliente: {nombre_cliente}")
print(f"Días de estadía: {dias_estadia}")
print(f"costo total: ${costo_total:.2f}")
print(f"Vista al mar: {'Sí' if vista_al_mar else 'No'}")
