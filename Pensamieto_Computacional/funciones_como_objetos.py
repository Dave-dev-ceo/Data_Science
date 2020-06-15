# Argumentos en otras funciones
def sumar_dos(n):
    return n +2
def multiplicar_por_dos(n):
    return n * 2

def aplicar_operacion(f , numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados
        

nums = [1, 2, 3]
resul_suma=aplicar_operacion(sumar_dos,nums)
result_multi=aplicar_operacion(multiplicar_por_dos,nums)
print(resul_suma,result_multi)

#Funciones con expresiones
sumar = lambda x, y : x + y

sum_lambda=sumar(2,5)

print(sum_lambda)


#Funciones en estructuras de datos
def aplicar_oper(num):
    operacio = [abs, float]

    result = []
    for operacion in operacio:
        result.append(operacion(num))
    return result

a = aplicar_oper(-2)
print (a) 