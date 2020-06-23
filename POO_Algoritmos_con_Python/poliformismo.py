class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print(f'Soy {self.nombre} y voy caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f'Soy {self.nombre} y voy moviendome en bicicleta')



def main():

    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Karen')
    ciclista.avanza()



if __name__ == "__main__":
    main()