print("*** Aplicación de Salud y Fitness ***")

#Consrantes 
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 #Valor aproximado, son kilocalorias

#Pedimos los valores al usuario
nombre_usuario = input("Cual es tu nombre? ")
pasos_diarios = int(input("Cuantos pasos has dado hoy? "))

#Verificar si el usuario ha alcanzado su meta de pasos
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = "Sí" if meta_alcanzada else "No"
#Calcular las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO
#Mostrar los resultados
print(f"\nHola {nombre_usuario}, has dado {pasos_diarios} pasos hoy.")
print(f"¿Has alcanzado tu meta de pasos diarios? {meta_alcanzada_txt}")
print(f"Has quemado aproximadamente {calorias_quemadas:.2f} kilocalorias hoy.")



