import plotly.graph_objects as go

class VisualizadorSankey:
    def __init__(self, altura=500, tamanho_fonte=12):
        self.altura = altura
        self.tamanho_fonte = tamanho_fonte

    def _extrair_dados_do_grafo(self, grafo):
        nos = list(grafo.nodes())
        no_para_indice = {no: i for i, no in enumerate(nos)}

        origens = []
        alvos = []
        valores = []
        nomes_produtos = []

        for origem, destino, dados in grafo.edges(data=True):
            origens.append(no_para_indice[origem])
            alvos.append(no_para_indice[destino])
            valores.append(dados['quantidade']) 
            nomes_produtos.append(dados['produto'])

        return nos, origens, alvos, valores, nomes_produtos

    def gerar_grafico(self, grafo, titulo="Fluxo de Energia e Massa da Rede"):
        nos, origens, alvos, valores, nomes_produtos = self._extrair_dados_do_grafo(grafo)

        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=nos,
            ),
            link=dict(
                source=origens,
                target=alvos,
                value=valores,
                label=nomes_produtos
            )
        )])

        fig.update_layout(
            title_text=titulo, 
            font_size=self.tamanho_fonte,
            height=self.altura
        )  
        return fig

visualizador = VisualizadorSankey()