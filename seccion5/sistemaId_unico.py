#Programa de sistema de generador de id unico
from random import randint 

print("*** Generador ID Unico ***")

nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
anio_nacimiento = input("Ingresa anio que naciste: ")

# Normalizar los valores
nombre_2 = nombre_usuario.strip().upper()[0:2]
apellido_2 = apellido_usuario.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:]

#Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# id unico
id_unico = f"{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}"

print(f"""\nHola {nombre_usuario}
Tu nuevo id generado por el sistema es:
{id_unico}
Vuelve Pronto!
""""")
