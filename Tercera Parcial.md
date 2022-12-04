# **Ejercicios realizados en clase (Elixir)**
---
## Utilización del Shell
#### Cargar en la terminal el Shell (iex)
```
C:\>iex
Interactive Elixir (1.10.4) - press Ctrl+C to exit (type h() ENTER for he
lp)
iex()>
```
#### Se pueden realizar expresiones que se evaluarán al presionar
```
iex()> 10 + 5<enter>
15
iex()> 10 +<enter>
...()> 5<enter>
15<enter>
```
#### Se pueden escribir múltiples expresiones, retornando siempre el último valor calculado
```
iex()> 10+5;11+1
12
```
#### Utilizar valores calculados anteriores en el shell
```
iex(1)> 3 + 4
7
iex(2)> v 1
7
iex(3)> v(1)
7
iex(4)> v(1) + 11
18
iex(5)> v(4)
18
```
#### Cuando nos equivocamos en una expresión y no permite continuar el shell
```
iex(1)> (23+4
...(1)>
...(1)> sd
...(1)> as
iex(1)> #iex:break
iex(1)>
```
#### Para salir del Shell se puede mediante CTRL+C o escribiendo System.halt
```
iex()> System.halt

C:\>
```
#### Para pedir ayuda del Shell
```
iex()> h
* IEx.Helpers

Welcome to Interactive Elixir. You are currently
seeing the documentation for the module `IEx.Helpers`
which provides many helpers to make Elixir's shell
more joyful to work with.
.
.
.
  * `b/1` - prints callbacks info and docs for a given module
  * `c/1` - compiles a file
  * `c/2` - compiles a file and writes bytecode to the given path
.
.
.

To learn more about IEx as a whole, type `h(IEx)`.
```
#### Para ver la ayuda específica de alguna opción (macro) se puede indicar como h opción, o h(opción)
```
iex()> h b
* defmacro b(term)

Prints the documentation for the given callback function.

It also accepts single module argument to list
all available behaviour callbacks.
```
---
## Variables
#### Elixir es un lenguaje de programación dinámico
```
iex()> dia_semana = 7 <fija (binds) el valor>
7 <resultado de la última expresión>
iex()> dia_semana <expresion que retorna el valor de la variable>
7 <valor de la variable>
iex()> dia_semana * 2
14
```
#### Características de las variables
```
variable_valida
esta_variable_tambien_es_valida
esta_tambien_1
estaEsValidaPeroNoRecomendada
No_es_valida
nombre_valido?
claro_que_si!
```
#### Inmutabilidad
```
iex()> dia_semana = 5 <se establece el valor inicial>
5
iex()> dia_semana <verificación>
5 <>
iex()> dia_semana = 7 <se refija el valor inicial>
7 <>
iex()> dia_semana <se verifica el efecto de la refijación>
7 <>
```
---
## Estructura del código (módulos y funciones)
#### Función puts
```
iex()> IO.puts("Hola Mundo")
Hola Mundo
:ok
```
#### Función sin argumentos
##### Código:
```elixir
defmodule HolaMundo do
  def mensaje do
    IO.puts("Hola Mundo")
  end
end
```
##### Salida:
```
iex()> HolaMundo.mensaje
Hola Mundo
:ok
```
#### Función con argumentos
##### Código:
```elixir
defmodule Calculadora do
  def suma(n1,n2) do
    n1 + n2
  end
end
```
##### Salida:
```
C:\>iex porta.ex
Interactive Elixir (1.10.4) - press Ctrl+C to exit (type h() ENTER for help)
iex()> Calculadora.suma(4,5)
9
```
#### Un archivo puede contener varios módulos
##### Código:
```elixir
defmodule Calculadora do
  def suma(n1,n2) do
    n1 + n2
  end
end

defmodule Areas do
  def area_cuadrado(l) do
    l*l
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Areas, Calculadora]
iex()> Areas.area_cuadrado(5)
25
iex()> Calculadora.suma(12,5)
17
```
#### Reglas de los módulos
##### Código:
```elixir
defmodule Geometria.Cuadrado do
  def perimetro(l) do
    4*l
  end
end

defmodule Geometria.Rectangulo do
  def perimetro(l1,l2) do
    2*l1 + 2*l2
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Geometria.Cuadrado, Geometria.Rectangulo]
iex()> Geometria.Cuadrado.perimetro(4)
16
iex()> Geometria.Rectangulo.perimetro(4,2)
12
```
#### También se pueden anidar de la siguiente forma
##### Código:
```elixir
defmodule Geometria do
  defmodule Cuadrado do
    def perimetro(l) do
      4*l
    end
  end
  defmodule Rectangulo do
    def perimetro(l1,l2) do
      2*l1 + 2*l2
    end
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Geometria, Geometria.Cuadrado, Geometria.Rectangulo]
iex()> Geometria.Cuadrado.perimetro(4)
16
iex()> Geometria.Rectangulo.perimetro(4,2)
12
```
#### Las funciones pueden expresarse de manera condensada
##### Código:
```elixir
defmodule Geometria do
  def perimetro_cuadrado(l), do: 4*l
  def perimetro_rectangulo(l1,l2), do: 2*l1 + 2*l2
end
```
##### Salida:
```
iex()> c("porta.ex")
[Geometria]
iex()> Geometria.perimetro_cuadrado(4)
16
iex()> Geometria.perimetro_rectangulo(4,3)
14
```
#### Los paréntesis en los argumentos son opcionales
##### Salida:
```
[Geometria]
iex()> Geometria.perimetro_cuadrado 4
16
iex()> Geometria.perimetro_rectangulo 4,3
14
```
#### Invocaciones internas de una función no requieren del prefijo del nombre del módulo
##### Código:
```elixir
defmodule Geometria do
  def perimetro1(l), do: cuadrado(l)
  def perimetro2(l), do: Geometria.cuadrado(l)
  def cuadrado(l), do: 4*l
end
```
##### Salida:
```
iex()> c("porta.ex")
[Geometria]
iex()> Geometria.perimetro1(4)
16
iex()> Geometria.perimetro2(4)
16
iex()> Geometria.cuadrado(4)
16
```
#### Visibilidad de funciones
##### Código:
```elixir
defmodule TestPublicoPrivado do
  def funcion_publica(msg) do
    IO.puts("#{msg} publico")
    funcion_privada(msg)
  end
  
  defp funcion_privada(msg) do
    IO.puts("#{msg} privado")
  end
end
TestPublicoPrivado.funcion_publica("este es un mensaje")
```
##### Salida:
```
iex> c("porta.ex")
este es un mensaje publico
este es un mensaje privado
[TestPublicoPrivado]
```
#### Módulo Geometría
##### Código:
```elixir
defmodule Geometria do
  def perimetro1(l), do: cuadrado(l)
  def perimetro2(l), do: Geometria.cuadrado(l)
  defp cuadrado(l), do: 4*l
end
```
##### Salida:
```
iex()> c("porta.ex")
[Geometria]
iex()> Geometria.perimetro1(4)
16
```
#### Operador pipeline
##### Código:
```elixir
defmodule Operaciones do
  def suma(n1,n2), do: n1 + n2
  def cuadrado(n), do: n * n
end
```
##### Salida:
```
iex()> 4 |> Operaciones.suma(5) |> Operaciones.cuadrado
81
iex()> Operaciones.suma(4,5) |> Operaciones.cuadrado
81
```
#### Mediante un módulo test que realice las pruebas se podría realizar de la siguiente forma
##### Código:
```elixir
defmodule Operaciones do
  def suma(n1,n2), do: n1 + n2
  def cuadrado(n), do: n * n
end

defmodule Test do
  def start do
    4 |> Operaciones.suma(5) |>Operaciones.cuadrado
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Operaciones, Test]
iex()> Test.start
81
```
---
## Estructura del código
#### Aridad (arity)
##### Código:
```elixir
defmodule Rectangulo do
  def area(l) do
    l * l
  end
  def area(l1,l2) do
    l1 * l2
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Rectangulo]
iex()> Rectangulo.area(2)
4
iex()> Rectangulo.area(2,5)
10
```
#### Haciendo que una función dependa de otra de diferente aridad, se podría realizar lo siguiente
##### Código:
```elixir
defmodule Calculadora do
  def suma(n) do
    suma(n,0)
  end
  def suma(n1,n2) do
    n1 + n2
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Calculadora]
iex()> Calculadora.suma(6)
6
iex()> Calculadora.suma(13,2)
15
```
### Argumentos por defecto
#### Se pueden especificar argumentos por defecto mediante el operador
##### Código:
```elixir
defmodule Calculadora do
  def suma(n1,n2 \\ 0) do
    n1 + n2
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Calculadora]
iex()> Calculadora.suma(3)
3
iex()> Calculadora.suma(7,3)
10
```
#### Se puede utilizar cualquier combinación de argumentos por defecto
##### Código:
```elixir
defmodule Calculadora do
  def funcion(n1,n2 \\ 0, n3 \\ 1, n4, n5 \\ 2) do
    n1 + n2 + n3 + n4 + n5
  end
end
```
##### Salida:
```
iex()> c("porta.ex")
[Calculadora]
iex()> Calculadora.funcion(4,5)
12
iex()> Calculadora.funcion(4,5,6)
18
iex()> Calculadora.funcion(4,5,6,7)
24
iex()> Calculadora.funcion(4,5,6,7,8)
30
```
### Imports
##### Código:
```elixir
import ModuloImportado

defmodule ModuloMain do
  def main do
    IO.puts("Funcion main")
    funcion_importada("Esta funcion es importada")
  end
end
```
#### Creamos el Módulo a importar modsec.ex
##### Código:
```elixir
defmodule ModuloImportado do
  def funcion_importada(msg) do
    IO.puts(msg)
  end
end
```
#### Compilamos en iex la función a importar
```
iex> c("modsec.ex")
[ModuloImportado]
```
#### Compilamos en iex la función que va a importar
```
iex> c("main.ex")
[ModuloMain]
```
#### Ejecutamos la función main
##### Salida:
```
iex> ModuloMain.main()
Funcion main
Esta funcion es importada
:ok
```
#### Si no se quiere importar el módulo, se puede utilizar de manera directa indicando el módulo y la función esto es:
##### Código:
```elixir
defmodule ModuloMain do
  def main do
    IO.puts("Funcion main")
    ModuloImportado.funcion_importada("Esta funcion es importada")
  end
end
```
##### Salida:
```
iex()> c("main.ex")
[ModuloMain]
iex()> ModuloMain.main()
Funcion main
Esta funcion es importada
:ok
```
### Alias
#### Se puede utilizar alias como alternativa a import, permite hacer una referencia a un módulo con otro nombre
##### Código:
```elixir
defmodule ModuloMain do
  alias ModuloImportado, as: MI
  
  def main do
    IO.puts("Funcion main")
    MI.funcion_importada("Esta funcion es importada con alias")
  end
end
```
##### Salida (bash):
```
iex(10)> c("main.ex")
[ModuloMain]
iex()> ModuloMain.main()
Funcion main
Esta funcion es importada con alias
:ok
```
### Atributos de módulo
#### Existen los atributos en tiempo de compilación (Mientras están cargados)
##### Código:
```elixir
defmodule Geometria do
  @pi 3.141592
  def area(r) do
    r*r*@pi
  end
  def circunferencia(r) do
    2 * r * @pi
  end
end
```
##### Salida:
```
iex> c("main.ex")
[Geometria]
iex> alias Geometria, as: G
Geometria
iex> G.area(4)
50.265472
iex> G.circunferencia(4)
25.132736
```
#### Elixir permite el registro de atributos, que se almacenarán en el archivo binario
##### Código:
```elixir
defmodule Geometria do
  @moduledoc "Calcula el area y el perimetro de un circulo"
  
  @pi 3.141592

  @doc "calcula el area del circulo"
  def area(r), do: r*r*@pi
  
  @doc "calcula el perimetro de un circulo"
  def circunferencia(r), do: 2 * r * @pi
end
```
##### Salida (comprobación):
```
iex> Code.fetch_docs(Geometria)
{:docs_v1, 2, :elixir, "text/markdown",
  %{"en" => "Calcula el area y el perimetro de un circulo"}, %{},
  [
    {{:function, :area, 1}, 6, ["area(r)"],
    %{"en" => "calcula el area del circulo"}, %{}},
    {{:function, :circunferencia, 1}, 9, ["circunferencia(r)"],
    %{"en" => "calcula el perimetro de un circulo"}, %{}}
  ]}
iex> h Geometria
* Geometria

Calcula el area y el perimetro de un circulo
iex> h Geometria.area
* def area(r)

calcula el area del circulo
iex> h Geometria.circunferencia
* def circunferencia(r)

calcula el perimetro de un circulo
```
### Tipos de datos
#### Numeros
```
iex> 3
3
iex> is_number(3)
true
iex> 3.5
3.5
iex> is_number(3.5)
true
```
#### Integer
```
iex> is_integer(3)
true
iex> is_float(3)
false
iex> i 34 #inspect
Term
  34
Data type
  Integer
Reference modules
  Integer
Implemented protocols
  IEx.Info, Inspect, List.Chars, String.Chars
```
#### Float
```
iex> is_integer(3.5)
false
iex> is_float(3.5)
true
iex> i(3.5)
Term
  3.5
Data type
  Float
Reference modules
  Float
Implemented protocols
  IEx.Info, Inspect, List.Chars, String.Chars
```
#### Notación científica
```
iex> 3.25555e-3
0.00325555
iex> 3.25555e3
3255.55
iex>i 3.25555e3
Term
  3255.55
Data type
  Float
Reference modules
  Float
Implemented protocols
  IEx.Info, Inspect, List.Chars, String.Chars
```
#### Operaciones aritméticas
```
iex> 5 * 4 / 3 + 2 - 5
3.666666666666668
iex> 5/4
1.25
iex> 5/5
1.0
iex> div(5,5)
1
iex> rem(5,5)
0
```
#### Piso de un número flotante
```
iex> trunc(5/2)
2
iex> floor(5/2)
2
```
#### Techo (cielo) de un número flotante
```
iex> round(5/2)
3
iex> ceil(5/2)
3
```
#### Números binarios
```
iex> 0b10101001111
1359
```
#### Números octales
```
iex> 0o74754
31212
```
#### Números hexadecimales
```
iex> 0xFFFF
65535
```
#### Azucar Sintáctica para los números
```
iex> 1_000_000
1000000
iex> 1_000_000.123
1000000.123
```
### Atoms
```
iex> :atom
:atom
iex> is_atom(:atom)
true
iex> is_atom(:es_un_atom)
true
iex> is_atom(:"es un atom")
true
iex> i :ok
Term
  :ok
Data type
  Atom
Reference modules
  Atom
Implemented protocols
  IEx.Info, Inspect, List.Chars, String.Chars
```  
#### Un atom consta de dos partes (texto-valor)
```
iex> var_atom = :atom
:atom
iex> var_atom
:atom
iex> :atom = var_atom
:atom
```
#### Un atom se puede nombrar con mayúscula inicial
```
iex> is_atom(Un_atom)
true
iex> Un_atom = Elixir.Un_atom
Un_atom
```
#### Atomos como booleanos
```
iex> is_atom(true)
true
iex> is_boolean(true)
true
iex> is_boolean(:true)
true
iex> is_boolean(:atom)
false
iex> :true == true
true
iex> :false == false
true
```
### Atoms and, or y not
```
iex> true and true
true
iex> true and false
false
iex> true or true
true
iex> true or false
true
iex> not false
true
iex> not true
false
iex> not not true
```
### Nil
#### Similar al null de otros lenguajes
```
iex> is_atom(nil)
true
iex> is_atom(:nil)
true
iex> nil == :nil
true
```
#### || Retorna la primera expresión verdadera
```
iex> false || nil || 5 || true
5
iex> false || nil || 5 || false || true
5
iex> false || nil || false || false || true || 5
true
```
#### && Retorna la segunda siempre y cuando la primera lo sea también
```
iex> false && 5
false
iex> nil && 5
nil
iex> true && 5
5
iex> true && true
true
iex> 5 && true
true
iex> true && 5 && 4
4
iex> false && 5 && 4
false
iex> true && false && 4
false
iex> true && 4 && false
false
```
#### !! Retorna la negación de la expresión sin importar el tipo de dato
```
iex> !true
false
iex> !false
true
iex> !5
false
iex> !nil
true
iex> not !4
true
iex> !(5+4)
false
```
### Tuplas
#### Permiten agrupar elementos fijos
```
iex>persona = {"Emilio", 19}
{"Emilio", 19}
iex> i {"Alex", 19}
Term
  {"Emilio", 19}
Data type
  Tuple
Reference modules
  Tuple
Implemented protocols
  IEx.Info, Inspect
```
#### Para extraer elementos se usa la función elem
```
iex> nombre = elem(persona, 0)
"Emilio"
iex> nombre
"Emilio"
iex> edad = elem(persona,1)
19
iex> edad
19
```
#### Para modificar un elemento se usa la función put_elem
```
iex> put_elem(persona,0,"Emilio")
{"Emilio", 19}
```
#### Las tuplas son inmutables, por lo que no se modifica
```
iex> persona
{"Emilio", 19}
```
#### Si se necesita cambiar, hay que almacenar el cambio en otra variable, o en la misma si ya no se desea conservar los valores
```
iex> persona = put_elem(persona,0,"Emilio")
{"Emilio", 19}
iex> persona
{"Emilio", 19}
```
### Listas
#### Manejo dinámico de datos
```
iex> numeros_pares = [2,4,6,8,10]
[2, 4, 6, 8, 10]
iex> i [2, 4, 6, 8, 10]
Term
  [2, 4, 6, 8, 10]
Data type
  List
Reference modules
  List
Implemented protocols
  Collectable, Enumerable, IEx.Info, Inspect, List.Chars, String.Chars
iex> length(numeros_pares)
5
```
#### Obtener un elemento de la lista mediante la función Enum.at/2
```
iex> Enum.at(numeros_pares,4)
10
iex> Enum.at(numeros_pares,5)
nil
```
#### Se puede saber si x elemento pertenece a una lista con operador in
```
iex> 2 in numeros_pares
true
iex> 12 in numeros_pares
false
```
#### Módulo List
```
iex> List.replace_at(numeros_pares,4,12)
[2, 4, 6, 8, 12]
iex> numeros_pares
[2, 4, 6, 8, 10]
iex> nuevos_pares = List.replace_at(numeros_pares,4,12)
[2, 4, 6, 8, 12]
iex> numeros_pares = List.replace_at(numeros_pares,4,12)
[2, 4, 6, 8, 12]
```
#### Insertar un elemento
```
iex> numeros_pares
[2, 4, 6, 8, 12]
iex> numeros_pares = List.insert_at(numeros_pares,4,10)
[2, 4, 6, 8, 10, 12]
iex> numeros_pares = List.insert_at(numeros_pares,-1,14)
[2, 4, 6, 8, 10, 12, 14]
```
#### Concatenar dos listas
```
iex> numeros_naturales = [1,2,3,4] ++ [5,6,7,8]
[1, 2, 3, 4, 5, 6, 7, 8]
iex> numeros_naturales
[1, 2, 3, 4, 5, 6, 7, 8]
```
#### Recursion sobre listas
```
iex> []
[]
iex> [1|[]]
[1]
iex> [1|[2|[]]]
[1, 2]
iex> [1|[2|[3|[]]]]
[1, 2, 3]
iex> [1|[2|[3|[4|[]]]]]
[1, 2, 3, 4]
iex> [1|[2,3,4]]
[1, 2, 3, 4]
```
#### Funciones hd y tl
```
iex> numeros = [1,2,3,4,5]
[1, 2, 3, 4, 5]
iex> hd(numeros)
1
iex> tl(numeros)
[2, 3, 4, 5]
iex> [head | tail] = numeros
[1, 2, 3, 4, 5]
iex> head
1
iex> tail
[2, 3, 4, 5]
```
#### Agregar elementos a una lista
```
iex> numeros = [0 | numeros]
[0, 1, 2, 3, 4, 5]
iex> numeros
[0, 1, 2, 3, 4, 5]
```
### Mapas
#### Par llave-valor
```
iex> persona = %{:nombre => "Emilio", :edad => 19, :trabajo =>"paseador"}
%{edad: 19, nombre: "Emilio", trabajo: "paseador"}
iex> persona
%{edad: 19, nombre: "Emilio", trabajo: "paseador"}
iex> consonantes = %{:z => "zeta", :m => "eme", :x => "equis", :b => "be"}
%{b: "be", m: "eme", x: "equis", z: "zeta"}
iex> consonantes = %{:z => "zeta", :m => "eme", :x => "equis", :b => "be", :n => "ene"}
%{b: "be", m: "eme", n: "ene", x: "equis", z: "zeta"}
iex> consonantes = %{:z => "zeta", :m => "eme", :x => "equis", :b => "be", :n => "ene", :a => "aaaa"}
%{a: "aaaa", b: "be", m: "eme", n: "ene", x: "equis", z: "zeta"}
```
#### Otra forma de representar los mapas
```
iex> %{nombre: "Emilio", paterno: "Manzano", edad: 19}
%{edad: 19, nombre: "Emilio", paterno: "Manzano"}
```
#### Acceder a un elementro a través de su llave
```
iex> persona = %{:nombre => "Emilio", :edad => 19, :trabajo =>"paseador"}
%{edad: 19, nombre: "Emilio", trabajo: "paseador"}
iex> persona[:nombre]
"Emilio"
iex> persona[:edad]
19
iex> persona[:apellido]
nil
```
#### Ventajas de usar atoms como llave
```
iex> persona.nombre
"Emilio"
iex> persona.edad
19
iex> persona.apellido
** (KeyError) key :apellido not found in: %{edad: 19, nombre: "Emilio", trabajo: "paseador"}
```
#### 
