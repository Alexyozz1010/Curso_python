print("MAQUINA DE SNACKS")

snacks = [
    {"id": 1, "nombre": "Papas fritas", "precio": 1.50, "cantidad": 10},
    {"id": 2, "nombre": "Galletas", "precio": 2.50, "cantidad": 20},
    {"id": 3, "nombre": "Chocolate", "precio": 1.25, "cantidad": 15},
    {"id": 4, "nombre": "Coca Cola", "precio": 1.00, "cantidad": 25},
]

carrito = []


def mostrar_snacks():
    print("--- Snacks disponibles ---")
    for snack in snacks:
        print(
            f"Id: {snack.get('id')}, Nombre: {snack.get('nombre')}, Precio: ${snack.get('precio')}, Cantidad: {snack.get('cantidad')}"
        )


def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get("id") == id_buscar:
            return snack
    return None


def comprar_snack():
    print("--- Comprar snack ---")
    id_comprar = int(input("Ingrese el id del snack: "))
    snack = buscar_snack_por_id(id_comprar)

    if snack is not None:
        if snack.get("cantidad") > 0:
            snack["cantidad"] -= 1
            carrito.append(snack)
            print(f"Agregaste: {snack.get('nombre')}")
        else:
            print("No hay stock disponible")
    else:
        print("Snack no encontrado")


def mostrar_ticket():
    print("\n--- Ticket de compra ---")
    total = 0

    for snack in carrito:
        print(f"{snack.get('nombre')} - ${snack.get('precio')}")
        total += snack.get("precio")

    print(f"Total a pagar: ${total}")


if __name__ == "__main__":
    while True:
        print(
            """\n--- MENU ---
1. Mostrar snacks
2. Comprar snack
3. Ver ticket
4. Salir"""
        )

        opcion = int(input("Seleccione: "))

        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print("Hasta luego")
            break
        else:
            print("Opción inválida")
