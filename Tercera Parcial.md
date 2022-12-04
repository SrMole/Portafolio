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
C:\>iex porta.exs
Interactive Elixir (1.10.4) - press Ctrl+C to exit (type h() ENTER for help)
iex(1)> Calculadora.suma(4,5)
9
```
#### Un archivo puede contener varios módulos.
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
iex()> c("porta.exs")
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
iex()> c("porta.exs")
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
iex(7)> c("porta.exs")
[Geometria, Geometria.Cuadrado, Geometria.Rectangulo]
iex(8)> Geometria.Cuadrado.perimetro(4)
16
iex(9)> Geometria.Rectangulo.perimetro(4,2)
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
iex()> c("porta.exs")
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
iex()> c("porta.exs")
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
iex> c("porta.exs")
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
  def cuadrado(l), do: 4*l
end
```
##### Salida:
```
iex()> c("porta.exs")
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
iex()> c("modulo01.ex")
[Operaciones, Test]
iex()> Test.start
81
```
