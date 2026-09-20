from solucion.empleados import Empleado, Contratado, DePlanta

class Empresa:
    def __init__(self):
        self._empleados = []

    @property
    def empleados(self):
        return tuple(self._empleados)

    def agregar_empleado(self, empleado):
        if not isinstance(empleado, Empleado):
            raise TypeError("No se ingresó un empleado valido")
        self._empleados.append(empleado)

    def total_sueldo_a_pagar(self):
        return sum(empleado.sueldo() for empleado in self.empleados)