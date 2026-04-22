from src.models.modelador_de_rede import modelador
import networkx as nx
import pandas as pd

# Teste Unitário para ver se o gráfico não possui ciclos
def test_grafo_sem_ciclos():
    dados = {
        'origem': ['A', 'B', 'C'],
        'destino': ['B', 'C', 'D'],
        'produto': ['X', 'Y', 'Z'],
        'quantidade': [1000, 900, 1500],
        'tipo_fluxo': ['Co_Produto', 'Normal', 'Entrada_Externa'],
        'transformidade': [2, 5, 8]
    }
    df = pd.DataFrame(dados)
    grafo = modelador.construir_grafo(df)

    assert nx.is_directed_acyclic_graph(grafo)