def factorial(n):
    """ Calcuala el factorial de n
        n int > 0 
        returns n!
    """
    print(n)
    if n==1:
        return 1

    return n * factorial(n-1)

n = int(input('Escribe un numero entero para calcular su factorial: '))
print(factorial(n))