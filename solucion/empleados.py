from abc import ABC, abstractmethod

class Empleado:
    def __init__(self, nombre, apellido, dni, categoria):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.categoria = categoria
        self.horas_trabajadas_por_dia = []

    def sueldo(self):
        return self.categoria.calcular_sueldo(self.horas_trabajadas_por_dia)

    def efectivizar(self, nivel):
        self.categoria = DePlanta(nivel)

    def precarizar(self, horas_minimas_dirias, costo_hora):
        self.categoria = Contratado(horas_minimas_dirias, costo_hora)

class Categoria(ABC):

    @abstractmethod
    def calcular_sueldo(self, horas_trabajadas_por_dia):
        pass

class Contratado(Categoria):
    def __init__(self, horas_minimas_diarias, costo_hora):
        self.horas_minimas_diarias = horas_minimas_diarias
        self.costo_hora = costo_hora

    def calcular_sueldo(self, horas_trabajadas_por_dia):
        return self.costo_hora * self.horas_minimas_diarias * sum(1 for x in horas_trabajadas_por_dia if x >= self.horas_minimas_diarias)