from abc import ABC, abstractmethod

class Empleado:
    def __init__(self, nombre, apellido, dni, categoria):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.categoria = categoria
        self.horas_trabajadas_este_mes = []

    def sueldo(self):
        return self.categoria.calcular_sueldo(self.horas_trabajadas_este_mes)

    def efectivizar(self, horas_minimas_dirias, costo_hora):
        self.categoria = DePlanta(horas_minimas_dirias, costo_hora)

    def precarizar(self, nivel):
        self.categoria = Contratado(nivel)

class Categoria(ABC):

    @abstractmethod
    def calcular_sueldo(self, horas_trabajadas_este_mes):
        pass

class Contratado(Categoria):
    def __init__(self, horas_minimas_diarias, costo_hora):
        self.horas_minimas_diarias = horas_minimas_diarias
        self.costo_hora = costo_hora

    def calcular_sueldo(self, horas_trabajadas_este_mes):
        return sum(map(lambda x: x * self.costo_hora, filter(lambda x: x > self.horas_minimas_diarias, horas_trabajadas_este_mes)))