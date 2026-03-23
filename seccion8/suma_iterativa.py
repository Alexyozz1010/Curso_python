print("*** Suma iterativa ***")

MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    print(f"\n(acumulador_suma + numero -> {acumulador_suma} + {numero})", end=" ")
    acumulador_suma += numero 
    numero += 1

    print(f"Suma parcial acumulada: {acumulador_suma}\n")

print(f"\nLa suma de los números del 1 al {MAXIMO} es: {acumulador_suma}")