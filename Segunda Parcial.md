# **Ejercicios resueltos en clase (Dart)**
---
## *Ejercicio 1*
#### 1.1 Descripción del ejercicio:
Diseñar una calculadora con el uso de funciones
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
void main() {
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

#### 2.2 Código:
```dart

```
#### 2.3 Implementación:
```dart

```
#### 2.4 Salida:
```

```
---
## *Ejercicio 3*
#### 3.1 Descripción del ejercicio:

#### 3.2 Código:
```dart

```
#### 3.3 Implementación:
```dart

```
#### 3.4 Salida:
```

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

#### 5.2 Código:
```dart

```
#### 5.3 Implementación:
```dart

```
#### 5.4 Salida:
```

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
