print("*** SISTEMA DE AUTENTICACION ***")

usuario_valido = "admin"
password_valido = "123"

usuario_ingresado = input("Cual es tu usuario?: ")
password_ingresado = input("Cual es tu contraseña?: ")

son_datos_correctos = (usuario_ingresado.strip() == usuario_valido and password_ingresado.strip() == password_valido)

print(f"Datos son correctos? {son_datos_correctos}")