# Error de principiante

respuesta_usuario = "False"

#La funcion solo evalua si el string "" esta vacio
es_verdad = bool(respuesta_usuario)
print(f"El valor es: {es_verdad}")

#Output: El valor es: True
# ¿Por que? Porque el string "False" tiene 5 letras. No esta vacio.

# Forma corecta de valor vacio:
texto_vacio = ""
print(bool(texto_vacio)) #False