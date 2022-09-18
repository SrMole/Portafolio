# Primera Parcial: Tópicos avanzados de programación
---
## Ejercicios resueltos en clase
---
### Ejercicio 1.
#### Descripción del ejercicio:
Escribir una función que reciba un mensaje y un nombre y escriba en pantalla "mensaje-nombre"
#### Código:
```python
def mensaje(msg:str,nom:str)->str:
    return f"{msg} {nom}"
```
#### Entrada:
```python
mensaje("Hola","Emilio")
```
#### Salida:
```python
'Hola Emilio'
```
---
### Ejercicio 2.
#### Descripción del ejercicio:
Escribir una función que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser: "Hola 'nombre' tienes 'edad' años"
#### Código:
```python
def mensaje2(nom:str,edad:int)->str|int:
    return f"Hola {nom} tienes {edad} años"
```
#### Entrada:
```python
mensaje2("Emilio",19)
```
#### Salida:
```python
'Hola Emilio tienes 19 años'
```
---
### Ejercicio 3.
#### Descripción del ejercicio:
Escribir una función que reciba el año actual y el año de nacimineto, usando la funcion anterior envia esta como argumento y obtenga el mensaje: "Hola 'nombre' tienes 'edad' años"
#### Código:
```python
def edad(act:int,naci:int)->int:
    return act-naci

def mensaje2(nom:str,edad:int)->str|int:
    return f"Hola {nom} tienes {edad} años"
```
#### Entrada:
```python
mensaje2("Emilio",edad(2022,2003))
```
#### Salida:
```python
'Hola Emilio tienes 19 años'
```
---
### Ejercicio 4.
#### Descripción del ejercicio:
Hacer una funcion que reciba el nombre de un persona el año de nacimiento y el año actual retornando el mensaje "Hola 'nombre' tienes 'edad' años"
#### Código:
```python
def mensaje(nom:str,act:int,naci:int)->int|str:
    return f"Hola {nom}, tienes {act-naci} años"
```
#### Entrada:
```python
mensaje("Emilio",2022,2003))
```
#### Salida:
```python
'Hola Emilio tienes 19 años'
```
---
### Ejercicio 5.
#### Descripción del ejercicio:
Hacer una función que genere una tabla de multiplicar recibiendo como argumento el ancho, la cantidad de números y el número a multiplicar
### Código:
```python
def tabla(an:int,can:int,tab:int)->int:
    for a in range(1,can+1):
        print(f"{a:^{an}} x {tab:^{an}} = {a*tab:^{an}}") 
```
#### Entrada:
```python
tabla(10,4,2)
```
#### Salida:
```python
    1      x     2      =     2     
    2      x     2      =     4     
    3      x     2      =     6     
    4      x     2      =     8    
```
---
### Ejercicio 6.
#### Descripción del ejercicio:
Hacer una función que genere n tablas de multiplicar recibiendo como argumentos el número de tablas, el número hasta donde se va a multiplicar y el ancho
### Código:
```python
def producto (a:int,b:int)->int:
    return a*b

def tablas(m:int, n:int, fmt:int)->int:
    for i in range(1,m+1):
        tabla1(n,i,fmt)
    
def tabla1(n:int,t:int,fmt:int)->int:
    for i in range(1,n+1):
        print(f"{t:^{fmt}}x{i:^{fmt}}={producto(i,t):^{fmt}}")
```
#### Entrada:
```python
tablas(3,5,10)
```
#### Salida:
```python
    1     x    1     =    1     
    1     x    2     =    2     
    1     x    3     =    3     
    1     x    4     =    4     
    1     x    5     =    5     
    2     x    1     =    2     
    2     x    2     =    4     
    2     x    3     =    6     
    2     x    4     =    8     
    2     x    5     =    10    
    3     x    1     =    3     
    3     x    2     =    6     
    3     x    3     =    9     
    3     x    4     =    12    
    3     x    5     =    15     
```
---
### Ejercicio 7.
#### Descripción del ejercicio:
Rellenar una lista con los números naturales del 1 al 10
### Código:
```python
lista_nat = []
for i in range(1,11):
    lista_nat.append(i)
```
#### Entrada:
```python
print(lista_nat)
```
#### Salida:
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
---
