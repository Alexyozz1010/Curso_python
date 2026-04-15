# Programa generador de email
print(""" 
    Generador de Emails
""")

nombre = input("Ingrese su nombre: ")
apellidos = input("Ingresa tu apellido: ")
empresa = input("Ingresa nombre de la empresa: ")
extension_dominio = input("Ingresa el dominio(Ej: .com.ec): ")

# Normalizamos los valores recibidos

nombre = nombre.strip().lower().replace(" ", "." )
apellidos = apellidos.strip().lower().replace(" ", "." )
empresa = empresa.strip().lower().replace(" ", ".")
extension_dominio = extension_dominio.strip().lower().replace(" ", ".")

#Generar el email
email = f"{nombre}.{apellidos}@{empresa}{extension_dominio}"
print(f"""
    Tu nuevo email generado por el sistema es:
    {email}
    Congratulations!!!!!!!!
""")