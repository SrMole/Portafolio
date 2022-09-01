#%%
n1=10
msg="hola"

print(n1,msg)
print(str(n1)+msg)

#fstrings
print(f"{n1} {msg}")

#%%
#Hacer una funcion que reciba el nombre de un persona
#el año de nacimiento y el año actual retornando el mensaje
#"Hola <nombre>, tienes <edad> años"

def mensaje(nom:str,act:int,naci:int)->int|str:
    return f"Hola {nom}, tienes {act-naci} años"

if __name__=="__main__":
    a=str(input("Dame tu nombre: "))
    b=int(input("Dame el año actual: "))
    c=int(input("Dame tu año de nacimiento: "))
    
    print(mensaje(a,b,c))

# %%
def edad(act:int,naci:int)->int:
    return act-naci
    
def mensaje2(nom:str,act:int,naci:int)->str|int:
    return f"Hola {nom}, tienes {edad(act,naci)} años"

if __name__=="__main__":
    print(mensaje2("Emilio",2022,2009))

# %%

Alumnos=["Hugo","Paco", "Luis", "Lupita"]
print(f"alumnos: {Alumnos}")

#sets (no se pueden repetir los valores)
for i in range(len(Alumnos)):
    print(f"Alumno {i+1}: {Alumnos[i]}")


# %%

#diccionarios
alumnos = {"nombre": "Hugo","Materia1": 10, "Materia2": 9}
print(f"Alumnos: {alumnos}")
print(f"Alumno: {alumnos['nombre']}")
print(f"Alumno: {alumnos['Materia1']}")

# %%

#comprobacion de que los valores en set no se repiten
numeros_list = [3,4,2,4,5,3,4,5,4,3,4,5,3,2,4,5,3,4,3]
numeros_set = {3,4,2,3,4,5,2,1,3,4,2,3,5,3,2,3,5,3,2,4}
print(numeros_list)
print(numeros_set)


# %%

e = ["Nombre", "Est Dat", "Prog Func", "Ingles"]
ALumnos = ["Hugo", "Paco", "Luis", "Lupita"]
m_e_d = [10,10,8,10]
m_p_f = [8,8,8.5,7]
m_i = [7,9,9,10]

ancho = 15
print(f"{e[0]:^{ancho}}{e[1]:^{ancho}}{e[2]:^{ancho}}{e[3]:^{ancho}}")
for i in range(len(ALumnos)):
    print(f"{ALumnos[i]:<{ancho}}{m_e_d[i]:^{ancho}}{m_p_f[i]:^{ancho}}{m_i[i]:^{ancho}}")
# %%
