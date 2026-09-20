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

### Crear la clase abstracta Categoria y sus clases hijas Contratado y DePlanta
Ya que ambos son categorías y deben cumplir con el método que calcula el sueldo, hago una clase llamada Categoria de la que heredan las dos. De esta forma, puedo chequear que cuando se asigne una categoría, lo que se asigne sí sea una categoría.

### Crear una clase contendora de Empleados.
Ya que como requerimiento se deben realizar métodos que trabajan con la información de todos los empleados.

### Utilizar Strategy para la relación de dependencia. 
En la relación de dependencia voy a usar el patrón Strategy, porque necesito que se pueda calcular el sueldo de un empleado en base a su categoría, pero sin tener un método que utilice un IF para saber qué tipo de cálculo debe hacer, esa elección la quiero desacoplar del empleado y dejar que la categoría en sí se encargue de qué algoritmo va a implementar. También, porque si fuera una herencia, si quisiera cambiar la categoría del empleado, debería crear un nuevo objeto que tenga los mismos datos personales y las horas que el empleado, pero con una categoría diferente. No voy a usar el patrón State, porque no cambia el tipo de categoría en base a un valor o puntaje, sino que cambia arbitrariemnte según lo que requiere el usuario del sistema (es decir, se puede precarizar o efectivizar arbitrariamente).

### Utilizar Enum para los niveles de los empleados de planta.
Como todos los empleados de planta calculan de la misma manera su sueldo y lo único que tienen los niveles de diferente es el valor de la hora de trabajo (el cual es exactamente el mismo para TODOS los que pertenezcan a un mismo nivel), crear clases diferentes para cada nivel sería innecesario. Se puede crear una clase Nivel, que herede de Enum, que asocie a cada nivel con un valor.

## Preguntas teóricas
Responder las siguientes preguntas sin realizar ningún código:
1. ¿Es necesario realizar cambios sobre la lógica inicial del método total_sueldos_a_pagar cuando se agreguen nuevos tipos de empleados? Justificar conceptualmente.

Rta: No es necesario realizar ningún cambio. La lógica del cálculo de sueldos no está dentro de la clase Empresa, ni tampoco dentro de la clase Empleado, sino que está dentro de cada categoría. No se necesita saber qué tipo de categoría tiene un empleado ya que todas las categorías implementan un método que calcula el sueldo y que se llama de la misma manera (debido a que así lo pide la clase abstracta Categoria). Si se quiere agregar una nueva clase, solo se debe crear una clase hija de Categoría que implemente este método a su manera; de esta manera extendemos las funcionalidades, sin modificar la lógica de la Empresa.

2. ¿Qué concepto del paradigma orientado a objetos se rompería al utilizar IF en el método optimizar_sueldos? Justificar conceptualmente.

Rta: Si se utilizara IF en este método, estaríamos haciendo que la clase Empresa sepa demasiado de los detalles de los empleados, aumentando el acoplamiento. También, hace menos escalable el código, ya que tendriamos que considerar cómo puede cambiar este IF si agregamos una nueva categoría. Al poner dejar la decisión en manos de la categoría en sí, aprovechamos el polimorfismo y cada Empleado reacciona dependiendo de qué tenga en su atributo categoría, permitiendo que la categoría decida si quedarse igual o cambiar.