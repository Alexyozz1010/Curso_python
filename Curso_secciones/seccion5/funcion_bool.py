# Programa: Funcion bool

# 1. Números (int y float)

print(bool(0)) # False(el vacio numerico)
print(bool(0.0)) # False
print(bool(42)) # True (Existe valor)

#2. Texto(Strings)
#Cadena vacia = Nada = False
print(bool("")) #False

# Cadena con espacio o texto = Algo = True
print(bool(" ")) # True porque contiene algo asi sea un espacio
print(bool("Hola")) #True

#None (Ausencia total)
vacio = None
print(bool(vacio)) #False

print(bool(True))