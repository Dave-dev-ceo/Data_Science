import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    n = 100`

    start= time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start= time.time()
    factorial_r(n)
    end = time.time()
    print(end - start)


