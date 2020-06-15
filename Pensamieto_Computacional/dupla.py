#Las duplas son inmutables pero si reasignadas

my_tuple = ()
print(type(my_tuple))

my_tuple1 = (1, 'dos',True)
print(my_tuple1)
print(my_tuple1[0])
print(my_tuple1[1])
print(my_tuple1[2])

#Dupla de 1 solo valor

my_dupla_valor = (1,)
print(my_dupla_valor)

my_dupla_valores = (2, 3, 4)

# Sumar Duplas. Hubo una reasignacion 
my_dupla_valor += my_dupla_valores
print(my_dupla_valor)

# Desempaquetar duplas
w, x , y, z = my_dupla_valor
print(w)
print(x)
print(y)
print(z)

#Regresar varios valores de una funcion
def coordenadas():
    return (3,8)

coordenada = coordenadas()
print(coordenada)
x, y = coordenadas()
print(x)
print(y)
