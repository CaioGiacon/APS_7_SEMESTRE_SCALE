import networkx as nx

class ModeladorRede:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def construir_grafo(self, dataframe):
        self.grafo = nx.from_pandas_edgelist(
            dataframe,
            source='origem',
            target='destino',
            edge_attr=['produto', 'quantidade', 'tipo_fluxo', 'transformidade'],
            create_using=nx.DiGraph()
        )
        return self.grafo
    
modelador = ModeladorRede()