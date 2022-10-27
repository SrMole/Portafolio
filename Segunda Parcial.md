# **Ejercicios resueltos en clase (Dart)**
---
## *Ejercicio 1*
#### 1.1 Descripción del ejercicio:
Diseña una calculadora utilizando el uso de funciones.
#### 1.2 Código:
```dart
String leerDatos(String mensaje) {
  print(mensaje);
  String data = (stdin.readLineSync()!);
  return data;
}

String calculadora(String op, int n1, int n2) {
  if (op == "+") {
    return "$n1 + $n2 = ${suma(n1, n2)}";
  } else if (op == "-") {
    return "$n1 - $n2 = ${resta(n1, n2)}";
  } else if (op == "*") {
    return "$n1 * $n2 = ${multi(n1, n2)}";
  } else if (op == "/") {
    return "$n1 / $n2 = ${divi(n1, n2)}";
  } else {
    return "Operación inválida";
  }
}

int suma(int num1, int num2) => num1 + num2;
int resta(int num1, int num2) => num1 - num2;
int multi(int num1, int num2) => num1 * num2;
int divi(int num1, int num2) => num1 ~/ num2;
```
#### 1.3 Implementación:
```dart
void main(List<String> args) {
  String op = leerDatos("Indica la operación [+,-,*,/]");
  int num1 = int.parse(leerDatos("Dame el primer número"));
  int num2 = int.parse(leerDatos("Dame el segundo número"));
  print("${calculadora(op, num1, num2)}");
}
```
#### 1.4 Salida:
```
Indica la operación [+,-,*,/]
+
Dame el primer número
3
Dame el segundo número
4
3 + 4 = 7
```
---
## *Ejercicio 2*
#### 2.1 Descripción del ejercicio:
Diseña el reporte de un estudiante usando clases.
#### 2.2 Código:
```dart
class Estudiante {
  String? Carrera;
  int? Semestre;
  String? NoCuenta;
  void reporte() {
    print("Carrera: $Carrera");
    print("Semestre: $Semestre");
    print("Número de cuenta: $NoCuenta");
  }
}
```
#### 2.3 Implementación:
```dart
void main(List<String> args) {
  var estudiante1 = Estudiante();
  estudiante1.Carrera = "Ingeniería en Computación Inteligente";
  estudiante1.Semestre = 3;
  estudiante1.NoCuenta = "20184531";
  estudiante1.reporte();
}
```
#### 2.4 Salida:
```
Carrera: Ingeniería en Computación Inteligente
Semestre: 3
Número de cuenta: 20184531
```
---
## *Ejercicio 3*
#### 3.1 Descripción del ejercicio:
Diseña una calculadora utilizando el uso de clases.
#### 3.2 Código:
```dart
class Calculadora {
  int a = 0, b = 0;
  int suma(int a, int b) => a + b;
  int resta(int a, int b) => a - b;
  int multiplicacion(int a, int b) => a * b;
  double division(int a, int b) => a / b;
}
```
#### 3.3 Implementación:
```dart
void main(List<String> args) {
  Calculadora miSC = Calculadora();

  miSC.a = 5;
  miSC.b = 10;
  
  print("${miSC.a} + ${miSC.b} = ${miSC.suma(miSC.a, miSC.b)}");
  print("${miSC.a} - ${miSC.b} = ${miSC.resta(miSC.a, miSC.b)}");
  print("${miSC.a} * ${miSC.b} = ${miSC.multiplicacion(miSC.a, miSC.b)}");
  print("${miSC.a} / ${miSC.b} = ${miSC.division(miSC.a, miSC.b)}");
}
```
#### 3.4 Salida:
```
5 + 10 = 15
5 - 10 = -5
5 * 10 = 50
5 / 10 = 0.5
```
---
## *Ejercicio 4*
#### 4.1 Descripción del ejercicio:

#### 4.2 Código:
```dart

```
#### 4.3 Implementación:
```dart

```
#### 4.4 Salida:
```

```
---
## *Ejercicio 5*
#### 5.1 Descripción del ejercicio:
Diseña una clase "Vehiculo" la cual contiene las propiedades "Número de llantas, Color, Modelo y Marca" y los métodos "Arrancar, Correr y Frenar".
#### 5.2 Código:
```dart
class Vehiculo {
  int _Nollantas = 0;
  String _color = "";
  String _modelo = "";
  String _marca = "";

  Vehiculo(this._Nollantas, this._color, this._marca, this._modelo);
  Vehiculo.marca(this._marca);

  void arrancar() {
    print("Arrancando");
  }

  void correr() {
    print("Corriendo");
  }

  void frenar() {
    print("Frenando");
  }

  void showVehiculo() {
    print("Número de llantas: $_Nollantas");
    print("Color: $_color");
    print("Modelo: $_modelo");
    print("Marca: $_marca");
    arrancar();
    correr();
    frenar();
  }
}
```
#### 5.3 Implementación:
```dart
void main(List<String> args) {
  Vehiculo jeep = new Vehiculo(4, "Negro", "Gladiator", "Jeep");
  Vehiculo sentra = new Vehiculo.marca("Nissan");

  jeep.showVehiculo();
  print("");
  sentra.showVehiculo();
}
```
#### 5.4 Salida:
```
Número de llantas: 4
Color: Negro
Modelo: Jeep
Marca: Gladiator
Arrancando
Corriendo
Frenando

Número de llantas: 0
Color:
Modelo:
Marca: Nissan
Arrancando
Corriendo
Frenando
```
---
## *Ejercicio 6*
#### 6.1 Descripción del ejercicio:

#### 6.2 Código:
```dart

```
#### 6.3 Implementación:
```dart

```
#### 6.4 Salida:
```

```
---
