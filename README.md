# Practica Parcial 2024 Paradigmas de Programación 5

## Puntos importantes:
* **De TODOS los empleados conocemos**: nombre, apellido, DNI, tipo de relación de dependencia (contratado o de planta).

* **Empleados contratados**: Tienen un cantidad de horas mínimas diarias a cumplir y un costo por hora espeçifico de cada empleado según su contrato. Para el pago del sueldo solo se tienen en cuenta si cumplió o no con el mínimo (si es menos, no cobra ese día y si es más, cobra, pero lo mismo que si hubiera cumplido justo).

* **Empleados de planta**: Todos deben cumplir con las 200 horas mensuales, si hace más horas por de esa cantidad por mes, se paga el doble por cada hora extra. 
Se conoce la cantidad de horas que trabajó por día y cuál es su nivel (operativo, técnico o especialista). A todos los que tienen el mismo nivel, les pagan lo mismo.

* **Se puede cambiar de tipo de relación de dependencia**. No debe afectar a la información previa de horas y días trabajados.

## Decisiones tomadas:
### Crear la clase Empleado. 
Atributos: nombre, apellido, DNI, categoria y una colección de horas trabajadas por cada día (los elementos van a ser los totales de cada día, PERO SOLO DE ESTE MES).
Métodos: sueldo(), precarizar(), efectivizar()

## Crear la clase abstracta Categoria y sus clases hijas Contratado y DePlanta
Ya que ambos son categorías y deben cumplir con el método que calcula el sueldo, hago una clase llamada Categoria de la que heredan las dos. De esta forma, puedo chequear que cuando se asigne una categoría, lo que se asigne sí sea una categoría.

## Crear una clase contendora de Empleados.
Ya que como requerimiento se deben realizar métodos que trabajan con la información de todos los empleados.

## Utilizar Strategy para la relación de dependencia. 
En la relación de dependencia voy a usar el patrón Strategy, porque necesito que se pueda calcular el sueldo de un empleado en base a su categoría, pero sin tener un método que utilice un IF para saber qué tipo de cálculo debe hacer, esa elección la quiero desacoplar del empleado y dejar que la categoría en sí se encargue de qué algoritmo va a implementar. También, porque si fuera una herencia, si quisiera cambiar la categoría del empleado, debería crear un nuevo objeto que tenga los mismos datos personales y las horas que el empleado, pero con una categoría diferente. No voy a usar el patrón State, porque no cambia el tipo de categoría en base a un valor o puntaje, sino que cambia arbitrariemnte según lo que requiere el usuario del sistema (es decir, se puede precarizar o efectivizar arbitrariamente).