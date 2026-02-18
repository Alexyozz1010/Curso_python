#Programa: Aplicar el concepto de slicing

texto = "PROGRAMACION"

#1. Basico [inicio : fin]
print(texto[0:4]) #"PROG" el indice 4 no incluye

#2. Atajo desde el incio [: fin]

print(texto[:4]) #PROG Asume incio 0

#3. Atajo hasta el final [inicio:]

print(texto[8:]) #CION hasta el ultimo char

#4. Indice Negativos

print(texto[-4:]) #CION los ultimos 4

#5. Pasos [::paso] Invesrtir cadena

print(texto[::-1]) # Inivierte la palabra programacion