# Generador de emails
print("*** Generador de Emails ***")

#Nombre completo del usuario
nombre_completo = "Alex Yoza Tumbaco"
print(f"Nombre de Usuario: {nombre_completo}")
#Procesar o normalizar el nombre del usuario
nombre_normalizado = nombre_completo.strip()
#Reemplazar espacios en blancos por puntos
nombre_normalizado = nombre_normalizado.replace(" ", ".")
#Convertimos a minusculas
nombre_normalizado = nombre_normalizado.lower()
print(f"nombre usuario normalizado: {nombre_normalizado}")

# Datos de la empresa
nombre_empresa = " Globlal Mentoring "
print(f"\nNombre de la empresa: {nombre_empresa}")
extension_dominio = ".com.ec"
print(f"Extension del dominio: {extension_dominio}")
# Quitamos espacios en blancos y convertimos a mayusculas
nombre_empresa_normalizado = nombre_empresa.replace(" ", "").lower()
dominio_email = f"@{nombre_empresa_normalizado}{extension_dominio}"
print(f"Dominio del email normlaizado: {dominio_email}")
#Email final
email = f"{nombre_normalizado}{dominio_email}"
print(f"\nEmail final generado: {email}")