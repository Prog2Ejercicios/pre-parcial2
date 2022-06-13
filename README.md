# Ejercicios

## Ejercicio 1
Definir una función ``max_de_tres(nr1, nr2, nr3)``, que tome tres números como argumentos y devuelva el mayor de ellos.

## Ejercicio 2
Escribir una función ``es_vocal(caracter)`` que tome un carácter y devuelva un valor logico(True si es una vocal, de lo contrario devuelve False)

## Ejercicio 3
### 3.1 Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Implementar los siguientes métodos:
- Un constructor, donde los datos pueden estar vacíos.
- ``mostrar()``: Muestra los datos de la persona.
- ``esMayorDeEdad()``: Devuelve un valor lógico indicando si es mayor de edad.
### 3.2 Crear una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (es dinero asi que puede tener decimales). El titular será obligatorio y la cantidad es opcional. Implementar los siguientes métodos para la clase:
- Un constructor donde el titular es obligatorio y la cantidad opcional(0 por defecto)
- ``mostrar()``: Muestra los datos de la cuenta.
- ``ingresar(cantidad)``: se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
- ``retirar(cantidad)``: se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
## 3.3 Crear clase CuentaJoven, que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Implementar los siguientes metodos:

- Un constructor con bonificacion opcional(0 por defecto).
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
- Además la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
