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
mensaje2("Emilio",18)
```
#### Salida:
```python
'Hola Emilio tienes 18 años'
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
