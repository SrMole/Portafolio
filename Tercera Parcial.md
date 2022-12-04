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
```
