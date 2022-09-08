#%%
#funciones y mas funciones

ancho = 15
e = ["Nombre", "Est Dat", "Prog Func", "Ingles"]
ALumnos = ["Hugo", "Paco", "Luis", "Lupita"]
m_e_d = [9.45,10,8.32,10]
m_p_f = [8.89,8,8.5,7.5]
m_i = [7.23,9,9.86,10]

def reporte(an:int)->int:
    print(f"{e[0]:^{an}}{e[1]:^{an}}{e[2]:^{an}}{e[3]:^{an}}")
    for i in range(len(ALumnos)):
        print(f"{ALumnos[i]:*<{an}}{m_e_d[i]:+^{an}}{m_p_f[i]:#>{an}}{m_i[i]:~^{an}}")
    return 0;

if __name__=="__main__":
    print(reporte(ancho))
    

# %%

##:,d se usa para impirmir numeros con separacion con comas
numeroBig = 34234823479328912792
print(f"{numeroBig:,d}")
#:,.numf se usa para numeros con decimales (el :,.3f significa que se imprimiran 3 decimales)
numeroDeci = 3.141592678547
print(f"{numeroDeci:,.3f}")
#:e son para notaciones cientificas
print(f"{numeroDeci:e}")
#:% se usa para porcentajes
NumeroPor = 0.563695
print(f"{NumeroPor:%}")
#:.num% se usa para lo mismo que con los decimales (el :.2% siginifica que se imprimiran 2 decimales)
print(f"{NumeroPor:.2%}")
#:b se usa para covertir un numero al sistema binario
print(f"{25:b}")
#:c se usa para ver el codigo asking del numero
print(f"{45:c}")
#:x se usa para convertir un numero al sistema hexadecimal
print(f"{255:x}")
#:o se usa para convertir un numero al sistema octal
print(f"{49:o}")


# %%

#Escribe una funcion que genere una tabla de multiplicar
#recibiendo como argumento la cantidad de numeros y la tabla general


def tabla(an:int,can:int,tab:int)->int:
    for a in range(1,can+1):
        print(f"{a:^{an}} x {tab:^{an}} = {a*tab:^{an}}")
    return 0

if __name__=="__main__":
    ancho = 10
    b=int(input("Dame la cantidad de numeros que quieres multiplicar: "))
    c=int(input("Dame el numero por el que quieres multiplicar"))
    tabla(ancho,b,c)


# %%
#Hacer lo mismo perom ahora para n tablas

def producto (a:int,b:int)->int:
    return a*b

def tablas(m:int, n:int, fmt:int)->int:
    for i in range(1,m+1):
        tabla1(n,i,fmt)
    
def tabla1(n:int,t:int,fmt:int)->int:
    for i in range(1,n+1):
        print(f"{t:^{fmt}}x{i:^{fmt}}={producto(i,t):^{fmt}}")

if __name__=="__main__":
    tablas(3,7,25)
    
# %%
