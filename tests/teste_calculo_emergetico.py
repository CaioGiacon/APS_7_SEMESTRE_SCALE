import pytest
import pandas as pd
import io 
from src.facade.classe_facade import facade

def teste_calculo_emergetico():
    valor_esperado = 1.5e16
    
    dados_exemplo = pd.DataFrame({
        'origem': ['Fonte', 'Processo'],
        'destino': ['Processo', 'Etanol'],
        'produto': ['Insumo', 'Etanol'],
        'quantidade': [100, 50],
        'tipo_fluxo': ['Entrada_Externa', 'Normal'],
        'transformidade': [1.5e14, 1]
    })
    
    arquivo_exemplo = io.BytesIO(dados_exemplo.to_csv(index=False).encode('utf-8'))
    facade.salvar_arquivo(arquivo_exemplo) 
    
    grafo_etanol = facade.buscar_registros('Etanol')
    assert grafo_etanol is not None, "O grafo falhou em ser gerado."
    
    emergia = facade.calculo_emergetico(grafo_etanol, 'Etanol')
    assert emergia == pytest.approx(valor_esperado)