print("*** Regresar una tupla de valores desde una funcion ***")

# Deficion funcion

def persona_mayusculas(nombre, apellido, edad):
    print(f"Esta funcion regresa varios valores(tupla)")
    return nombre.upper(), apellido.upper(), edad

#Probamos principal

nombre, apellido, edad = persona_mayusculas("Anaely", "Ochoa", 21)
print(f"Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")












