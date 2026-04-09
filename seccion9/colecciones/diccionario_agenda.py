print('*** Agenda de Contactos ***')

agenda = {
    'Carlos': {
        'telefono': '55667711',
        'email': 'carlos@mail.com',
        'direccion': 'Calle Principal 132'
    },
    'Maria': {
        'telefono': '99887733',
        'email': 'maria@mail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': '55139078',
        'email': 'pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(agenda)
print()

#Acceder a la información de un contacto específico
print(f"""Información de Maria:
Teléfono: {agenda["Maria"]["telefono"]}
Email: {agenda.get("Maria").get("email")}
Dirección: {agenda["Maria"]["direccion"]}
""")

#Agregar un nuevo contacto a la agenda
agenda["Ana"] = {
    'telefono': '55678392',
    'email': 'ana@mail.com',
    'direccion': 'Calle Salvador Diaz 321'
}

print(agenda)

#Eliminar un contacto de la agenda
agenda.pop("Pedro")
#del agenda["Carlos"]
print(agenda)

#Mostrar contacto con información completa
print("\nContactos de la Agenda")
for nombre, detalles in agenda.items():
    print(f"""Nombre: {nombre}
    Teléfono: {detalles["telefono"]}
    Email: {detalles["email"]}
    Dirección: {detalles["direccion"]}  
""")
