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