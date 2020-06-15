#las listas tiene side afects
my_list = [ 1, 2 ,3]

print(my_list[0])
print(my_list[:1])

my_list[0] = 'a'
print(my_list)

my_list.append(4)
print(my_list)

my_list.pop()
print(my_list)

#verificar que las listas apuntan al mismo lugar de memoria

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

#Creamos una lista de listas
c = [a, b]
print(c)

#modificamos a
a.append(8)
print(c)
#afectamos los dos

#CLONACION para evitar los side efects
# 1ra opcion es con lis()

a = [1,2,33]
print(id(a),a)
c = list(a)
print(id(c),c)

# 2da opcion es con ::

d = a[::]
print(id(d),d)

# List Comprehension

list_com = list(range(100))
print(list_com)

double = [i*2 for i in my_list]
print(double)

pares = [i for i in list_com if i % 2 == 0 ]
print(pares)