print(" *** Terminal Falsa ***")


while True:
    comando = input("kali@root:~$ ")
    if comando == "salir":
        print("Cerrando sesion...")
        break
    else:
        print(f"Comando '{comando}' no reconocido. Intente de nuevo.")
