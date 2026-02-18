print("***Operadores de Asignacion***")
numero = 5
print(f"El valor de numero = {numero}")
numero = 10
print(f"El valor de numero = {numero}")
cadena = "Saludos desde python"
print(f"Valor de la cadena: {cadena}")

# Asignacion multiple
x, y, z = 5, "hola", -9.15
print(f"valor de x= {x}, y= {y}, z= {z}")

# Asignacion encadenada
a = b = c = 10
print(f"El valor de a= {a}, b= {b}, c= {c}")

# Intercambio de valores de una variabole, si utilizar variables temporales
x, y = 5, 10
print(f"Valores iniciales x = {x}, y= {y}")
# Aplicando el concepto de asignacion multiple, intecambio de valores
x, y = y, x
print(f"invertir valores x= {x}, y= {y}")

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input("Ingresa tu nombre y apellido separados por coma: ").split(",")
print(f"tu nombre es: {nombre}, tu apellido es: {apellido}")