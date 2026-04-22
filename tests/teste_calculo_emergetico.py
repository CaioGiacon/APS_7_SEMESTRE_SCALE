import pytest
import pandas as pd
from src.facade.classe_facade import facade

def teste_calculo_emergetico():
    valor_esperado = 9.36e15
    grafo_etanol = facade.buscar_registros('Etanol')
    emergia = facade.calculo_emergetico(grafo_etanol, 'Etanol')

    assert emergia == pytest.approx(valor_esperado)