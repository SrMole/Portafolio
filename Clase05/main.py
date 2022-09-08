
#%%
#los array son estructuras de datos estaticas , se delcara el tama{o en tiempo de compilacion, son de un mismo tipo de dato
#las listas pueden usar cualqioer tipo de dato
#impimir listas
lista1 = [1,2,3,4]
print(lista1)
lista2 = [1,3.14,"a",True,[4,5,6],(1,2,3),{6,"a",5.4}]
print(lista2)

#len es una funcion que mide el tamaño de la lista
print(len(lista1))
print(len(lista2))
#seleccionar un elemento por indice (el numero es el lugar o espacio que tiene el elemento en la lista)
print(lista2[6])

lista_cal=[]
#.append es un metodo que agrega elemetos a la lista
lista_cal.append(5)
print(lista_cal)
#los elementos se agregan al final siempre (izquierda derecha)
lista_cal.append(8)
print(lista_cal)
#.insert  se usa para colocar un elemento en una ubicacion especifica
lista_cal.insert(1,6)
print(lista_cal)

#rellenar una lista con los numeros natirales del 1 al 10

lista_nat = []
for i in range(1,11):
    lista_nat.append(i)

print(lista_nat)

#indice negativo agarra el elemento de derecha a izquierda
print(lista1[-4])
print(lista1[-1])

#slices (rebanadas) imprime rangos de la lista
lista1=[1,2,3,4,5,6,7,8,9,10]
print(lista1[:])
print(lista1[0:5])
print(lista1[0:-1])
print(lista1[int(len(lista1)/2):])
print(lista1[:int(len(lista1)/2)])
print(lista1[3:7])
print(lista1[-7:-3])

#%%
#error frecuente al querer copiar una lista y cambiar algo
lista1 = [1,"dos",3,"cuatro"]
#print(lista1)
#lista1[1]=2
#print(lista1)
lista2=lista1
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
#cambios
lista2[1]=2
print("------------------------------")
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

# %%

#solucion
lista1 = [1,"dos",3,"cuatro"]
lista2 = lista1[:]
print(f"Direccion lista 1: {id(lista1)}")
print(f"Direccion lista 2: {id(lista2)}")
#cambios
lista1[1]=2
lista1[3]=4
lista2[0]="uno"
lista2[2]="tres"
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

# %%
#formas de agregar los elementos 5,6,7 a la lista 1

lista1 = [0,1,2,3,4]
for i in range(5,8):
    lista1.append(i)

print(lista1)

# %%

lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
lista1[5:]=lista2
print(lista1)

#%%

lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
lista1[5:]= [5,6,7]
print(lista1)

#%%

lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
lista1[len(lista1):]=lista2
print(lista1)

#%%

#se agregan los elementos de derecha a izquierda
lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
lista1[:0]=lista2
print(lista1)

# %%

lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
lista1.append(lista2)
print(lista1)

# %%

lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
lista1.extend(lista2)
print(lista1)

#%%

lista1 = [0,1,2,3,4,5,6,7]
#se usa del para borrar elementos de una lista
del lista1[0]
print(lista1)

# %%

#eliminar elementos con slices
lista1 = [0,1,2,3,4,5,6,7]
del (lista1[2:5])
print(lista1)

# %%
