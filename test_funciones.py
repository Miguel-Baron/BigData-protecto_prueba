"""
Your module description
"""
from funciones import sumar
from funciones import es_primo


def test_sumar():
    assert sumar(1,2) == 3
    assert sumar(5,2) == 7
    assert sumar(3,2) == 5

def test_es_primo():
    assert es_primo(5) is True
    assert es_primo(7) is True
    assert es_primo(8) is False