print("*** Generacion Ticket de Venta  ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio platanos: "))
descuento_porcentaje = int(input("Aplicar algun desceunto en (%)?: "))


#Calculo de subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#Aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100)

#Aplicar subtotal con descuento
subtotal_con_descuento= subtotal - descuento

#Calculo de subtotal con impuestos al 16%
impuesto = subtotal * 0.16

#Calcular total de la compra con impuestos
costo_total_compra= subtotal_con_descuento + impuesto

print(f"""
subtotal: ${subtotal:.2f} ({descuento_porcentaje}%)
subtotal con descuento: ${subtotal_con_descuento}
impuesto: ${impuesto:.2f}
costo total de la compra: ${costo_total_compra:.2f}
""")



