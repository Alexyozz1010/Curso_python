#Cadenas inmutables

animal = "Gato"

# animal[4] = "s" # Provoca error
# CORRECTO: concatenar (Sumar)
# Tomamos "Gato" + "S" y lo guardamos en una nueva variable

plural = animal + "s"

print(animal) # Salida: "Gato" (intacto)
print(plural) # Salida: "Gatos" (Nuevo objeto)

plural = f"{animal}s"
print(plural) # Salida: "Gatos" (Nuevo objeto)
