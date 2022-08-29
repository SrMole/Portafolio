#%%
#Escribir una funcion que reciba un mensaje y un nombre y escriba en pantalla "<mensaje><nombre>"

def mensaje(msg:str,nom:str)->str:
    return f"{msg} {nom}"

A=str(input("Dame un mensajeeeee: "))
b=str(input("Dame tu nombre: "))
mensaje(A,b)

# %%
#Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser: "Hola <nombre> tienes <edad> años"

def mensaje2(nom:str,edad:int)->str|int:
    return f"Hola {nom} tienes {edad} años"

A=str(input("Dame tu nombre: "))
b=int(input("Dame tu edad: "))
mensaje2(A,b)


# %%
#Escribir una funcion que reciba el año actual y el año de nacimineto, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años"

def edad(act:int,naci:int)->int:
    return act-naci

def mensaje2(nom:str,edad:int)->str|int:
    return f"Hola {nom} tienes {edad} años"

A=int(input("Dame el año actual: "))
b=int(input("Dame el año de tu nacimiento: "))
mensaje2("Emilio",edad(A,b))

# %%
