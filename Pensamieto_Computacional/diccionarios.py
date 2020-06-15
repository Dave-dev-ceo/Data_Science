my_dir = {
    'david' : 29,
    'karen' : 21,
    'paty' : 56,
}
print(my_dir['david'])

#Si no se encuentra una llave podremos regresar un valor por defecto
a = my_dir.get('No_existe',30)
print(a)

#para agregar una nueva llave y su valor hacemos
my_dir['benito'] = 57
print(my_dir)
my_dir['para_borrar'] = 100
print(my_dir)

#Para borrar un elmento 
del my_dir['para_borrar']
print(my_dir)

#para iterar en un direccionario

#iterar por LLAVES (keys)
for llave in my_dir.keys():
    print(llave)

#iterar en valores
for valores in my_dir.values():
    print(valores)

#iterar por llaves y valores
for llave, valores in my_dir.items():
    print(llave, valores)

#preguntar si una llave existe dentro del diccionario
if 'javier' in my_dir:
    print ('Existe en el diccionario')
else:
    print('no existe en el diccionario')

#Dir conberhesion
# Dictionary Comprehension