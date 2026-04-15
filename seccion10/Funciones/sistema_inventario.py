print("*** SISTEMA DE INVENTARIO con funciones ***")

# Inventario de almacen
inventario = [
    {"id": 1, "nombre": "Camisa", "precio": 25.99, "cantidad": 50},
    {"id": 2, "nombre": "Pantalones", "precio": 39.00, "cantidad": 30},
    {"id": 3, "nombre": "Zapatos", "precio": 49.99, "cantidad": 20},
]


# Funcion para mostrar el inventario
def mostrar_inventario():
    print("--- Inventario del Almaccen ---")
    for producto in inventario:
        print(
            f"Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, "
            f"Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}"
        )


def agregar_producto():
    # pass
    print("--- Agregar nuevo producto al inventario ---")
    id = int(input("Ingrese el id del producto: "))
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    cantidad_producto = int(input("Ingrese la cantidad del producto: "))
    nuevo_producto = {
        "id": id,
        "nombre": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto,
    }
    inventario.append(nuevo_producto)
    print("Producto agregado al inventario")


def buscar_producto_por_id():
    print("--- Buscar producto por id ---")
    id_buscar = int(input("Ingrese el id del producto a buscar: "))
    for producto in inventario:
        if producto.get("id") == id_buscar:
            print("\nInformacion del producto encontrado: ")
            print(
                f"Id: {producto.get('id')}, Nombre: {producto.get('nombre')},"
                f"Precio: ${producto.get('precio')},"
                f"Cantidad: {producto.get('cantidad')}"
            )
            return
    print("Producto no encontrado en el inventario.")


# Programa principal
if __name__ == "__main__":
    while True:
        print(
            f"""\n--- Menu ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por id
        4.Salir"""
        )
        opcion = int(input("Seleccione una opcion: "))
        # Validar la opcion seleccionada
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto_por_id()
        elif opcion == 4:
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opcion no valida, por favor seleccione una opcion del menu.")
