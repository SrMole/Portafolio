#%%
#una funcion siempre retorna un valor 
def suma(a,b):
    return a+b

#entry point en python
if __name__=="__main__":
    print(suma(9,2))

#%%
#id es la funcion para ver la direccion de memoria que tiene la variable
x=10
print(x,"addr: ",id(x))
x="hola"
print(x,"addr: ",id(x))

y=10
print(y,"addr: ",id(y))

#z se guarda en la misma direccion de memoria que x
z="hola"
print(z,"addr: ",id(z))
#si se cambia un caracter pasa a otra direccion de memoria
z="holA"
print(z,"addr: ",id(z))

#%%
#contador para ver que tienen diferentes direccions de memoria 
x=1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1
print(x,":",id(x))
x=x+1

#%%
def suma1(a,b):
    return a+b

#asignamos el tipo de dsto de la variable
def suma2(a:int,b:int)->int:
    return a+b

print(suma1(2,5))
print(suma2(3.2,3))
