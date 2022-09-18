# ***Primera Parcial: Tópicos avanzados de programación***
---
## **Ejercicios resueltos en clase**
---
### *Ejercicio 1*
#### 1.1 Descripción del ejercicio:
Escribir una función que reciba un mensaje y un nombre y escriba en pantalla "mensaje-nombre".
#### 1.2 Código:
```python
def mensaje(msg:str,nom:str)->str:
    return f"{msg} {nom}"
```
#### 1.3 Implementación:
```python
if __name__=="__main__":
    print(mensaje("Hola","Emilio"))
```
#### 1.4 Salida:
```
Hola Emilio
```
---
### Ejercicio 2
#### 2.1 Descripción del ejercicio:
Escribir una función que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser: "Hola 'nombre' tienes 'edad' años".
#### 2.2 Código:
```python
def mensaje2(nom:str,edad:int)->str|int:
    return f"Hola {nom} tienes {edad} años"
```
#### 2.3 Implementación:
```python
if __name__=="__main__":
    print(mensaje2("Emilio",19))
```
#### 2.4 Salida:
```
Hola Emilio tienes 19 años
```
---
### Ejercicio 3
#### 3.1 Descripción del ejercicio:
Escribir una función que reciba el año actual y el año de nacimineto, usando la funcion anterior envia esta como argumento y obtenga el mensaje: "Hola 'nombre', tienes 'edad' años".
#### 3.2 Código:
```python
def edad(act:int,naci:int)->int:
    return act-naci

def mensaje2(nom:str,edad:int)->str|int:
    return f"Hola {nom} tienes {edad} años"
```
#### 3.3 Implementación:
```python
if __name__=="__main__":
    print(mensaje2("Emilio",edad(2022,2003)))
```
#### 3.4 Salida:
```
Hola Emilio, tienes 19 años
```
---
### Ejercicio 4
#### 4.1 Descripción del ejercicio:
Hacer una función que reciba el nombre de una persona, el año de nacimiento y el año actual retornando el mensaje "Hola 'nombre' tienes 'edad' años".
#### 4.2 Código:
```python
def mensaje(nom:str,act:int,naci:int)->int|str:
    return f"Hola {nom}, tienes {act-naci} años"
```
#### 4.3 Implementación:
```python
if __name__=="__main__":
    print(mensaje("Emilio",2022,2003))
```
#### 4.4 Salida:
```
Hola Emilio tienes 19 años
```
---
### Ejercicio 5
#### 5.1 Descripción del ejercicio:
Hacer una función que imprima un reporte dadas cuatro listas (nombres, materias, calificaciones), recibiendo como argumento el ancho.
#### 5.2 Código:
```python
e = ["Nombre", "Est Dat", "Prog Func", "Ingles"]
ALumnos = ["Hugo", "Paco", "Luis", "Lupita"]
m_e_d = [9.45,10,8.32,10]
m_p_f = [8.89,8,8.5,7.5]
m_i = [7.23,9,9.86,10]

def reporte(an:int)->int:
    print(f"{e[0]:^{an}}{e[1]:^{an}}{e[2]:^{an}}{e[3]:^{an}}")
    for i in range(len(ALumnos)):
        print(f"{ALumnos[i]:<{an}}{m_e_d[i]:^{an}}{m_p_f[i]:^{an}}{m_i[i]:^{an}}")
```
#### 5.3 Implementación:
```python
if __name__=="__main__":
    reporte(15)
```
#### 5.4 Salida:
```
    Nombre         Est Dat       Prog Func       Ingles     
Hugo                9.45           8.89           7.23      
Paco                 10              8              9       
Luis                8.32            8.5           9.86      
Lupita               10             7.5            10   
```
---
### Ejercicio 6
#### 6.1 Descripción del ejercicio:
Hacer una función que genere una tabla de multiplicar recibiendo como argumento el ancho, la cantidad de números y el número a multiplicar.
#### 6.2 Código:
```python
def tabla(an:int,can:int,tab:int)->int:
    for a in range(1,can+1):
        print(f"{a:^{an}} x {tab:^{an}} = {a*tab:^{an}}")
```
#### 6.3 Implementación:
```python
if __name__=="__main__":
    tabla(10,4,2)
```
#### 6.4 Salida:
```
    1      x     2      =     2     
    2      x     2      =     4     
    3      x     2      =     6     
    4      x     2      =     8    
```
---
### Ejercicio 7
#### 7.1 Descripción del ejercicio:
Hacer una función que genere n tablas de multiplicar recibiendo como argumentos el número de tablas, el número hasta donde se va a multiplicar y el ancho.
#### 7.2 Código:
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
#### 7.3 Implementación:
```python
if __name__=="__main__":
    tablas(3,5,10)
```
#### 7.4 Salida:
```
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
### Ejercicio 8
#### 8.1 Descripción del ejercicio:
Rellenar una lista con los números naturales del 1 al 10.
#### 8.2 Código:
```python
lista_nat = []
for i in range(1,11):
    lista_nat.append(i)
```
#### 8.3 Implementación:
```python
if __name__=="__main__":
    print(lista_nat)
```
#### 8.4 Salida:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
---
### Ejercicio 9
#### 9.1 Descripción del ejercicio:
Agrega los elementos 5, 6, 7 a la lista 1.
#### 9.2 Código:
```python
lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
lista1[5:]=lista2
```
#### 9.3 Implementación:
```python
if __name__=="__main__":
    print(lista1)
```
#### 9.4 Salida:
```
[0, 1, 2, 3, 4, 5, 6, 7]
```
---
