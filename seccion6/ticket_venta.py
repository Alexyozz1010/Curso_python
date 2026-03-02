print("*** Generacion Ticket de Venta  ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio platanos: "))

#Calculo de subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#Calculo de subtotal con impuestos al 16%
impuesto = subtotal * 0.16

#Calcular total de la compra con impuestos
costo_total_compra= subtotal + impuesto

print(f"""
subtotal: ${subtotal:.2f}
impuesto: ${impuesto:.2f}
costo total de la compra: ${costo_total_compra:.2f}
""")

