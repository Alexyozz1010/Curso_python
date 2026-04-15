print("*** Calculadora ***")

salir = False

numero1 = float(input("Ingresa primer valor: "))
numero2 = float(input("Ingresa segundo valor: "))

while not salir:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado:.2f}")
    elif opcion == "2":
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado:.2f}")
    elif opcion == "3":
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicación es: {resultado:.2f}")
    elif opcion == "4":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado de la división es: {resultado:.2f}")
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == "5":
        salir = True
        print("Gracias por usar la calculadora, hasta luego")
    else:
        print("Opción no válida, por favor intente de nuevo.")
else:
    print("Has salido de la calculadora")