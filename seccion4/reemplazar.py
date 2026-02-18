# Programa reemplazar textos en python

mensaje = "Hola Mundo, Mundo"
print(mensaje)
#Reemplzar Todas las apariciones
nuevo = mensaje.replace("Mundo", "Python")

#Resultado: "Hola Python, Python"
print(nuevo)

#Reemplazar solo una vez
uno_solo = mensaje.replace("Mundo", "Dev", 1)
print(uno_solo)
#Salida "Hola Dev, Mundo"

