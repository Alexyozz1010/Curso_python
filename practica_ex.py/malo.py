# 1. Definimos nuestra lista de contraseñas (nuestro diccionario)
lista_posibilidad = ["qwerty", "123456", "admin", "iloveyou", "gatitoBeauty"]

# Imagina que esta es la clave real guardada en DVWA
clave_secreta = "gatitoBeauty" 

print("Iniciando ataque de fuerza bruta...\n")

# 2. El bucle: probará cada palabra de nuestro diccionario
for intento in lista_posibilidad:
    print(f"Probando contraseña: {intento}")
    
    # 3. El condicional: comprobamos si acertamos
    if intento == clave_secreta:
        print(f"[+++] ¡BINGO! Acceso concedido. La clave es: {intento}")
        break # Detenemos el ataque porque ya entramos
    else:
        print("[-] Clave incorrecta. Intentando la siguiente...")