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

    def optimizar_sueldos(self, horas_minimas_diarias, costo_hora):
        for empleado in self.empleados:
            empleado.precarizar(horas_minimas_diarias, costo_hora)

    def mejorar_sueldos(self, nivel):
        for empleado in self.empleados:
            empleado.efectivizar(nivel)
            
    def mejor_sueldo(self):
        if not self.empleados:
            return 0
        return max(empleado.sueldo() for empleado in self.empleados)