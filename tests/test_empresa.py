import pytest
from solucion.empresa import Empresa
from solucion.empleados import Empleado, Contratado, DePlanta, Nivel

@pytest.fixture
def empresa_con_empleados():
    empresa = Empresa()

    datos_empleados = [
        (33888999, Contratado(8, 6000.00)),
        (34888999, Contratado(8, 7000.00)),
        (35888999, Contratado(9, 7000.00)),
        (36888999, DePlanta(Nivel.OPERARIO)),
        (37888999, DePlanta(Nivel.OPERARIO)),
        (38888999, DePlanta(Nivel.OPERARIO)),
        (39888999, DePlanta(Nivel.TECNICO)),
        (32888999, DePlanta(Nivel.TECNICO)),
        (31888999, DePlanta(Nivel.ESPECIALISTA))
    ]

    for dni, categoria in datos_empleados:
        empresa.agregar_empleado(Empleado("Pepe", "Argento", dni, categoria))

    horas_mes_completo = [9] * 25 #9 horas, 25 dias, todos van a tener lo mismo
    for empleado in empresa.empleados:
        for horas_dia in horas_mes_completo:
            empleado.registrar_horas_del_dia(horas_dia)

    return empresa

def test_agregar_empleado():
    categoria = Contratado(8, 6000.00)
    empleado = Empleado("Pepe", "Argento", 33888999, categoria)
    empresa = Empresa()
    empresa.agregar_empleado(empleado)

    assert empresa.empleados[0] == empleado

@pytest.mark.parametrize("indice_empleado, sueldo_esperado", [
    (0, 1200000.00),  # Contratado (8hs, $6000)
    (1, 1400000.00),  # Contratado (8hs, $7000)
    (2, 1575000.00),  # Contratado (9hs, $7000)
    (3, 1500000.00),  # DePlanta OPERARIO
    (6, 2000000.00),  # DePlanta TECNICO
    (8, 2500000.00),  # DePlanta ESPECIALISTA
])

def test_calcular_sueldo_cada_uno(empresa_con_empleados, indice_empleado, sueldo_esperado):
    empleado = empresa_con_empleados.empleados[indice_empleado]

    assert empleado.sueldo() == sueldo_esperado

def test_calcular_total_sueldos_en_mes(empresa_con_empleados):
    assert empresa_con_empleados.total_sueldo_a_pagar() == 15175000.00

def test_obtener_mejor_sueldo(empresa_con_empleados):
    assert empresa_con_empleados.mejor_sueldo() == 2500000.00

def test_optimizar_sueldos(empresa_con_empleados):
    empresa_con_empleados.optimizar_sueldos(8, 7000.00)

    assert empresa_con_empleados.total_sueldo_a_pagar() == 12575000

def test_contratar_a_todos(empresa_con_empleados):
    empresa_con_empleados.contratar_a_todos(Nivel.OPERARIO)

    assert empresa_con_empleados.total_sueldo_a_pagar() == 15500000