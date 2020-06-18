#definicion de classes

""" class <nombre_de_la_clase> (<super_clase>):
    def __init__(self,<params>):
        <expresion>

    def <nombre_del_metodo>(self,<params>):
        <expresion> """

#Ejemplo
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, persona_a_saludar):
        return f'Hola {persona_a_saludar.nombre}, me llamo {self.nombre}.'

david = Persona('David',29)
print(david.nombre)

karen = Persona('Karen',21)
print(karen.nombre)

print(david.saluda(karen))