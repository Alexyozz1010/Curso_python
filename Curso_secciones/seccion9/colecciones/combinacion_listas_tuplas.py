print("*** Combinación de Listas y Tuplas ***")

#Definir una lista que almcena tuplas de productos

productos = [
    ("P001", "Camisa", 20.00),
    ("P002", "Jeans", 30.00),
    ("P003", "Sudadera", 40.00)
]

#Imprimir la informacion de cada producto
#y ademas calculamos el precio total
precio_total = 0


print("Información de productos: ")
for producto in productos:
    id, descripcion, precio = producto
    print(f"Producto; id = {id}, descripcion = {descripcion}, precio = ${precio}")
    precio_total += precio # Producto[2] tambien se puede usar para acceder al precio
print(f"\nPrecio total de los productos: ${precio_total}") 