from abc import ABC, abstractmethod
from enum import Enum

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

class Nivel(Enum):
    OPERARIO = 6000.00
    TECNICO = 8000.00
    ESPECIALISTA = 10000.00

class DePlanta(Categoria):
    def __init__(self, nivel):
        self.nivel = nivel

    def calcular_sueldo(self, horas_trabajadas_por_dia):
        total_horas_mes = sum(horas_trabajadas_por_dia)
        if total_horas_mes >= 200:
            return 200 * self.nivel.value + (total_horas_mes - 200) * 2 * self.nivel.value
        return 0

class Empleado:
    def __init__(self, nombre, apellido, dni, categoria):
        if not isinstance(dni, int) or dni <= 0:
            raise ValueError("El DNI del empleado debe ser un valor entero positivo")
        
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni
        self.categoria = categoria
        self._horas_trabajadas_por_dia = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def dni(self):
        return self._dni

    @property
    def categoria(self):
        return self._categoria

    @property
    def horas_trabajadas_por_dia(self):
        return tuple(self._horas_trabajadas_por_dia)
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre del empleado no puede estar vacío")
        self._nombre = nuevo_nombre

    @apellido.setter
    def apellido(self, nuevo_apellido):
        if not nuevo_apellido.strip():
            raise ValueError("El apellido del empleado no puede estar vacío")
        self._apellido = nuevo_apellido

    @categoria.setter
    def categoria(self, nueva_categoria):
        if not isinstance(nueva_categoria, Categoria):
            raise TypeError("La categoria ingresada no es valida")
        self._categoria = nueva_categoria

    def sueldo(self):
        return self.categoria.calcular_sueldo(self.horas_trabajadas_por_dia)

    def efectivizar(self, nivel):
        self.categoria = DePlanta(nivel)

    def precarizar(self, horas_minimas_dirias, costo_hora):
        self.categoria = Contratado(horas_minimas_dirias, costo_hora)

    def registrar_horas_del_dia(self, horas):
        if not (0 <= horas <= 24):
            raise ValueError("No se pueden registrar horas negativas o mayores a 24")
        self._horas_trabajadas_por_dia.append(horas)