print("*** Validación de contraseña ***")

password = input("Ingresa tu contraseña(6 caracteres): ")

while len(password) < 6:
    print(" El password debe tener al menos 6 caracteres, por favor intente de nuevo.")
    password = input("Ingresa tu contraseña(6 caracteres): ")
else:
    print("El valor de password es válido, gracias por ingresar tu contraseña.")