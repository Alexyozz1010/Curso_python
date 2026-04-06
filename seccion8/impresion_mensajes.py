print("*** Repeticion de mensajes ***")

mensaje = input("Ingresa un mensaje a repetir: ")
numero_de_repeticiones = int(input("Ingresa el número de repeticiones: "))

for _ in range(numero_de_repeticiones):
    #print(f"{i+1} - {mensaje}")
    print(mensaje)