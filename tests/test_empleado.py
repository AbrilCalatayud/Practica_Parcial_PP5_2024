from solucion.empleados import Empleado, Contratado, DePlanta, Nivel
import pytest

def test_crear_empleado_contratado():
    categoria_contratado= Contratado(8, 6000.00)
    empleado = Empleado("Pepe", "Argento", 33888999, categoria_contratado)

    assert empleado.nombre == "Pepe"
    assert empleado.apellido == "Argento"
    assert empleado.dni == 33888999
    assert empleado.categoria == categoria_contratado

def test_crear_empleado_de_planta():
    categoria_de_planta = DePlanta(Nivel.TECNICO)
    empleado = Empleado("Pepe", "Argento", 33888999, categoria_de_planta)

    assert empleado.nombre == "Pepe"
    assert empleado.apellido == "Argento"
    assert empleado.dni == 33888999
    assert empleado.categoria == categoria_de_planta

def test_crear_empleado_nombre_vacio():
    categoria = Contratado(8, 6000.00)
    with pytest.raises(ValueError):
        Empleado("", "Argento", 33888999, categoria)

def test_crear_empleado_apellido_vacio():
    categoria = Contratado(8, 6000.00)
    with pytest.raises(ValueError):
        Empleado("Pepe", "", 33888999, categoria)

def test_crear_empleado_dni_negativo():
    categoria = Contratado(8, 6000.00)
    with pytest.raises(ValueError):
        Empleado("Pepe", "Argento", -33888999, categoria)

def test_crear_empleado_categoria_invalida():
    categoria = "probando"
    with pytest.raises(TypeError):
        Empleado("Pepe", "Argento", 33888999, categoria)