import ops.cuadrado as c

def suma_cuadrado(a:int|float,b:int|float)-> int|float:
    return c.cuadrado(a) + c.cuadrado(b)

def sumar(a:int|float,b:int|float)-> int|float:
    return a+b

def restar(a:int|float,b:int|float)-> int|float:
    return a-b

def division(a:int|float,b:int|float)-> int|float:
    return a/b

def multiplicar(a:int|float,b:int|float)-> int|float:
    return a*b

def cuadrado(a:int|float)-> int|float:
    return a*a

