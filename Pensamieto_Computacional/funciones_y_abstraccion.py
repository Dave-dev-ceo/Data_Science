def nombre_completo(nombre, apellido, inversor = False):
    if inversor:
        return f'{apellido} , {nombre}'
    else:
        return f'{nombre} , {apellido}'

print(nombre_completo('David', 'Gonzalez'))
print(nombre_completo('David', 'Gonzalez', inversor=True))
print(nombre_completo(apellido = 'Gonzalez', nombre = 'David'))