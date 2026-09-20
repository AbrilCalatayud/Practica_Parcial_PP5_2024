from solucion.empleados import Contratado, DePlanta, Nivel
import pytest

def test_crear_categoria_contratado():
    categoria_contratado = Contratado(8, 6000.00)
    assert categoria_contratado.horas_minimas_diarias == 8
    assert categoria_contratado.costo_hora == 6000.00

def test_crear_categoria_contratado_horas_minimas_negativas():
    with pytest.raises(ValueError):
        Contratado(-8, 6000.00)

def test_crear_categoria_contratado_horas_minimas_mayores_24():
    with pytest.raises(ValueError):
        Contratado(25, 6000.00)

def test_crear_categoria_contratado_costo_hora_negativo():
    with pytest.raises(ValueError):
        Contratado(25, -6000.00)

def test_crear_categoria_de_planta_operario():
    categoria_de_planta = DePlanta(Nivel.OPERARIO)
    assert categoria_de_planta.nivel == Nivel.OPERARIO

def test_crear_categoria_de_planta_tecnico():
    categoria_de_planta = DePlanta(Nivel.TECNICO)
    assert categoria_de_planta.nivel == Nivel.TECNICO

def test_crear_categoria_de_planta_especialista():
    categoria_de_planta = DePlanta(Nivel.ESPECIALISTA)
    assert categoria_de_planta.nivel == Nivel.ESPECIALISTA

def test_crear_categoria_de_planta_nivel_invalido():
    with pytest.raises(TypeError):
        DePlanta("operario")
