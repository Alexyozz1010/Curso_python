print(" *** Recolector de de IP ***")

ips_objetivo = []

while True:
    ip = input("Ingresa un ip (o escribe 'fin' para terminar): ")
    if ip  == "fin":
        break
    ips_objetivo.append(ip)

print(f"Ips recolectadas: {ips_objetivo}")