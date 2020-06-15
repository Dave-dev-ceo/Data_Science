
def primera_letra (lista_de_palabras):
    primeras_letras =[]

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permite str vacios'

        primeras_letras.append(palabra[0])
    return primeras_letras

#primera_letra(['aasd',2])
#primera_letra(['',2])
primera_letra(['hola','mundo'])