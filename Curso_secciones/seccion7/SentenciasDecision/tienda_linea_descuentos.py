print("Bienvenido a la tienda en línea.")

MONTO_COMPRA_DESCUENTO = 1000

monto_compra = float(input("Ingrese el monto de su compra: "))
es_miembro = input("¿Es usted miembro del programa de fidelidad? (s/n): ")

descuento = 0
# Verificar si el monto de compra es mayor o igual al umbral para descuento
if monto_compra >= MONTO_COMPRA_DESCUENTO and es_miembro.strip().lower() == "s":
    descuento = 0.1  # Descuento del 10%
elif es_miembro.strip().lower() == "s":
    descuento = 0.05  # Descuento del 5% para miembros sin alcanzar el umbral
elif monto_compra >= MONTO_COMPRA_DESCUENTO:
    descuento = .03 #Descuento del 3%
else:
    descuento = 0  # No hay descuento

# Hacemos el cálculo del monto final después de aplicar el descuento
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(F"\nFelicidades, ha obtenido un descuento de {descuento*100:.0f}%.")
    print(f"Monto de la compra: ${monto_compra:.2f}")
    print(f"Monto del descuento: ${monto_descuento:.2f}")
    print(f"Monto final: ${monto_final:.2f}")
else:
    print("\nNo se ha aplicado ningún descuento.")
    print(f"Te invitamos a unirte a nuestro programa de fidelidad para obtener descuentos exclusivos en futuras compras.")
    print(f"Monto de la compra: ${monto_compra:.2f}")