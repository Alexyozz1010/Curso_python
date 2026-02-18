#SISTEMA EMPLEADO
print("*** SISTEMA DE EMPLEADO ***")
nombre_empleado = input("Ingresa tu nomre: ")
edad_empleado = int(input("Ingresa tu edad: "))
salario_empleado = float(input("Salario de empleado: "))
es_jefe_departamento = input("Eres jefe de departamento (si/no)? ")

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"

#Imprimir valores empleador
print("\nDatos empleado")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salrio: {salario_empleado:.2f}")
print(f"Es jefe de departamento?: {es_jefe_departamento}")