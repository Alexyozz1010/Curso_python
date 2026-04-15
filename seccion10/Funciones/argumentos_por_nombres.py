print("*** Funcion con argumentos por nombre ***")

def imprimir_persona(nombre, apellido=" ", edad= 0):
    print(f"Persona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}")

#Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona("Ricardo", "Quintana", 32)

#llamar la funcion usando argumentos por nombre
imprimir_persona(nombre="Carlos", apellido="Rojas", edad=28)

#LLmar la funcion usando argumentos por nombre, pero intercambiamos el orden
imprimir_persona(edad=28, apellido="Rojas", nombre="Carlos")

#Argumentos con valores por default
imprimir_persona(nombre="Carlos", apellido="Rojas")
imprimir_persona(apellido="Rojas", nombre="Carlos")