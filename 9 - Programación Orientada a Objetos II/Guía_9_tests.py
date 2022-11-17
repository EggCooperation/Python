import pytest
import Guía_9_clases_figuras


def test_herencias():
    assert issubclass(Guía_9_clases_figuras.Cuadrado, Guía_9_clases_figuras.Rectángulo)


def test_Rectángulo():
    rectángulo = Guía_9_clases_figuras.Rectángulo(5, 10)
    # getters
    assert rectángulo.base == 5
    assert rectángulo.área == 50
    assert rectángulo.altura == 10
    assert rectángulo.diagonal == 11.180339887498949
    # setters
    rectángulo.base = 5
    rectángulo.altura = 10
    # errores
    with pytest.raises(ValueError):
        rectángulo.base = 0

    with pytest.raises(ValueError):
        rectángulo.altura = 0
    

def test_Cuadrado():
    cuadrado = Guía_9_clases_figuras.Cuadrado(9)
    # getters
    assert cuadrado.lado == 9
    assert cuadrado.base == 9
    assert cuadrado.altura == 9
    assert cuadrado.área == 81
    assert cuadrado.diagonal == 12.727922061357855
    # setters
    cuadrado.base = 5
    assert cuadrado.altura == 5
    assert cuadrado.lado == 5
    cuadrado.altura = 6
    assert cuadrado.base == 6
    assert cuadrado.lado == 6
    cuadrado.lado = 10
    assert cuadrado.base == 10
    assert cuadrado.altura == 10
    # errores
    with pytest.raises(ValueError):
        cuadrado.lado = 0
    with pytest.raises(ValueError):
        cuadrado.base = 0
    with pytest.raises(ValueError):
        cuadrado.altura = 0
