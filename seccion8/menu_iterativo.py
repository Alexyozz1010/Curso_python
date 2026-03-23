print("*** Menú iterativo ***")

salir  = False
while not salir:
    print("\n1. Crear cuenta")
    print("2. Eliminar cuenta")
    print("3. Actualizar cuenta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Creando una nueva cuenta...")
    elif opcion == "2":
        print("Eliminando tu cuenta...")
    elif opcion == "3":
        print("Actualizando tu cuenta...")
    elif opcion == "4":
        salir = True
        print("Saliendo del menú...")
    else:
        print("Opción no válida, por favor intente de nuevo.")
else:
    print("Has salido del menú iterativo.")