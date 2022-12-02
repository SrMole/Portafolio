# **Ejercicios del PDF de Elixir**
---
## *Ejercicio 1*
#### 1.1 Descripción:
Función sin argumentos.
#### 1.2 Código:
```elixir
defmodule HolaMundo do
  def mensaje do
    IO.puts("Hola Mundo")
  end
end
```
#### 1.3 Salida:
```
iex()> HolaMundo.mensaje
Hola Mundo
:ok
```
---
## *Ejercicio 2*
#### 2.1 Descripción:
Función con argumentos.
#### 2.2 Código:
```elixir
defmodule Calculadora do
  def suma(n1,n2) do
    n1 + n2
  end
end
```
#### 2.3 Salida:
```
C:\>iex modulo01.ex
Interactive Elixir (1.10.4) - press Ctrl+C to exit (type h() ENTER for help)
iex(1)> Calculadora.suma(4,5)
9
```
---
## *Ejercicio 3*
#### 3.1 Descripción:
Archivo con varios módulos.
#### 3.2 Código:
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
#### 3.3 Salida:
```
iex()> c("modulo01.ex")
warning: redefining module Calculadora (current version defined in memory)
  modulo01.ex:1
[Areas, Calculadora]
iex()> Areas.area_cuadrado(4)
16
iex()> Calculadora.suma(5,5)
10
```
---
## *Ejercicio 4*
#### 4.1 Descripción:
Reglas de los módulos.
#### 4.2 Código:
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
#### 4.3 Salida:
```
iex()> c("modulo01.ex")
[Geometria.Cuadrado, Geometria.Rectangulo]
iex()> Geometria.Cuadrado.perimetro(4)
16
iex()> Geometria.Rectangulo.perimetro(4,2)
12
```
---
## *Ejercicio 5*
#### 5.1 Descripción:
Anidación de funciones.
#### 5.2 Código:
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
#### 5.3 Salida:
```
iex(7)> c("modulo01.ex")
warning: redefining module Geometria.Cuadrado (current version defined in memory)
  modulo01.ex:2
  
warning: redefining module Geometria.Rectangulo (current version defined in memory)
  modulo01.ex:7
  
[Geometria, Geometria.Cuadrado, Geometria.Rectangulo]
iex(8)> Geometria.Cuadrado.perimetro(4)
16
iex(9)> Geometria.Rectangulo.perimetro(4,2)
12
```
---
## *Ejercicio 6*
#### 6.1 Descripción:
Funciones expresadas de manera condensada.
#### 6.2 Código:
```elixir
defmodule Geometria do
  def perimetro_cuadrado(l), do: 4*l
  def perimetro_rectangulo(l1,l2), do: 2*l1 + 2*l2
end
```
#### 6.3 Salida:
```
Los paréntesis en los argumentos son opcionales.

iex()> c("modulo01.ex")
[Geometria]
iex()> Geometria.perimetro_cuadrado(4)
16
iex()> Geometria.perimetro_rectangulo(4,3)
14
```
---
## *Ejercicio 7*
#### 7.1 Descripción:
Las invocaciones internas de una función no requieren del prefijo del nombre del módulo
#### 7.2 Código:
```elixir
defmodule Geometria do
  def perimetro1(l), do: cuadrado(l)
  def perimetro2(l), do: Geometria.cuadrado(l)
  def cuadrado(l), do: 4*l
end
```
#### 7.3 Salida:
```
iex()> c("modulo01.ex")
[Geometria]
iex()> Geometria.perimetro1(4)
16
iex()> Geometria.perimetro2(4)
16
iex()> Geometria.cuadrado(4)
16
```
---
