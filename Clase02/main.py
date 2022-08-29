#%%
def suma(a:int|float,b:int|float)-> int|float:
    return a+b

def suma2(a,b):
    return a+b
    
if __name__=="__main__":
    print(suma("5","6")) 
    print(suma2(4,5)) 

#%%
import sumar as s
import restar as r
import division as d
import multiplicar as m
import cuadrado as c


if __name__=="__main__":
    print(s.sumar(5,3))
    print(r.restar(4,2))
    print(d.division(4,2))
    print(m.multiplicar(4,2))
    print(c.cuadrado(4))
    

#%%
from ops.operaciones import sumar,restar,division,multiplicar,suma_cuadrado

if __name__=="__main__":
    print(sumar(5,3))
    print(restar(4,2))
    print(division(4,2))
    print(multiplicar(4,2))
    print(suma_cuadrado(4,6))


# %%
import ops.operaciones as op

if __name__=="__main__":
    print(op.sumar(4,5))
    print(op.restar(4,5))
    print(op.division(4,5))
    print(op.multiplicar(4,5))
    print(op.suma_cuadrado(6,5))
    print(op.cuadrado(4))


# %%
import ops.sumar as s
import ops.restar as r
import ops.division as d
import ops.multiplicar as m
import ops.cuadrado as c

if __name__=="__main__":
    print(s.sumar(4,5))
    print(r.restar(4,5))
    print(d.division(4,5))
    print(m.multiplicar(4,5))
    print(c.cuadrado(4))

# %%
