print("*** Cajero automático ***")
salir = False
saldo = 1000

while not salir: 
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Selecciona un opcion: ")
    if opcion == "1":
        print(f"Tu saldo actual es {saldo:.2f}")
    elif opcion == "2":
        monto = float(input("Ingresa monto a retirar: "))
        if monto > saldo:
            print("Tu saldo es insuficiente")
        elif monto <= 0:
            print("Monto no válido, por favor ingrese un monto positivo.")
        else:
            saldo -= monto
            print(f"Has retirado {monto:.2f}, tu nuevo saldo es {saldo:.2f}")
    elif opcion == "3":
        monto = float(input("Ingresa monto a depositar: "))
        if monto <= 0:
            print("Monto no válido, por favor ingrese un monto positivo.")
        else:
            saldo += monto
            print(f" Has depositado {monto:.2f}, tu saldo actual es {saldo:.2f}")
    elif opcion =="4":
        salir = True
        print("Gracias por usar el cajero automático, hasta luego!")
    else:
        print("Opción no válida, por favor intente de nuevo.")
else:
    print("Has salido del cajero automatico")
