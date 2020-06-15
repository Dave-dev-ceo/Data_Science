# Rangos asi como las cadenas y las duplas son inmutables 

#range(inicio, fin, pasos)

my_range = range (1,5)

for i in my_range:
    print(i)

range_one = range(0, 7, 2)

range_two = range(0, 8, 2)

if range_one == range_two:
    print('Son dos rangos iguales por: equal value')

#Comparador logico "is" 
if range_one is range_two:
    print ('Los rangos son iguales')
else:
     print(f'Pero no son iguales en OBJECT EQUALITY porque en memoria range_ones es {id(range_one)} y range_two es {id(range_two)}')


# Generar una lista entre un rango con steps 

for i in range(1, 101, 2):
    print (i)