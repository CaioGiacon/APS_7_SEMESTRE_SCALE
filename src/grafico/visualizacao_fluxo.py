import plotly.graph_objects as go
import networkx as nx
import pandas as pd

class VisualizadorGrafoRede:
    def __init__(self, altura=600, tamanho_fonte=14):
        self.altura = altura
        self.tamanho_fonte = tamanho_fonte

    def gerar_grafico(self, grafo, titulo):
        posicoes = nx.spring_layout(grafo, k=0.5, iterations=50, seed=42)
        edge_x, edge_y = [], []
        middle_x, middle_y, middle_hover_text = [], [], []

        for origem, destino, dados in grafo.edges(data=True):
            x0, y0 = posicoes[origem]
            x1, y1 = posicoes[destino]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            
            middle_x.append((x0 + x1) / 2)
            middle_y.append((y0 + y1) / 2)
            
            produto = dados.get('produto', 'Desconhecido')
            quantidade = dados.get('quantidade', 0)
            texto = f"<b>{origem} -> {destino}</b><br>Produto: {produto}<br>Quantidade: {quantidade}"
            middle_hover_text.append(texto)

        trace_arestas = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )

        trace_meio_arestas = go.Scatter(
            x=middle_x, y=middle_y,
            mode='markers',
            hoverinfo='text',
            text=middle_hover_text,
            marker=dict(size=0.1, color='rgba(0,0,0,0)'),
            showlegend=False
        )

        node_x, node_y, node_text = [], [], []

        for no, dados in grafo.nodes(data=True):
            x, y = posicoes[no]
            node_x.append(x)
            node_y.append(y)
        
            valor = dados.get('emergia') or dados.get('valor') or dados.get('quantidade')
            
            if valor is not None:
                if isinstance(valor, (int, float)):
                    label = f"<b>{no}</b><br>({valor:.2e})"
                else:
                    label = f"<b>{no}</b><br>({valor})"
            else:
                label = f"<b>{no}</b>"
            
            node_text.append(label)

        trace_nos = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_text,
            textposition="top center",
            textfont=dict(
                family="Arial Black, sans-serif",
                size=self.tamanho_fonte,
                color="black"
            ),
            marker=dict(
                color='#1f77b4',
                size=35, 
                line=dict(width=2, color='white')
            )
        )

        fig = go.Figure(data=[trace_arestas, trace_meio_arestas, trace_nos],
                        layout=go.Layout(
                            title=dict(
                                text=titulo,
                                font=dict(size=18)
                            ),
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=60),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            height=self.altura,
                            plot_bgcolor="white"
                        ))
        
        return fig

visualizador = VisualizadorGrafoRede(altura=700)