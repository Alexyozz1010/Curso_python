print("*** Obtener coordenadas ***")

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

#llamar la funcion
resultado = obtener_coordenadas()
print(f"")

# unpacking de la tupla
x1, y1, z1 =  resultado 
print(f"cOORDENADAS X = {x1}, Y = {y1}, Z = {z1}")