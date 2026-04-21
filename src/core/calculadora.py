class CalculadoraEmergetica:
    def __init__(self):
        pass

    def verificar_no_atual(self, grafo, produto_alvo):
        for alvo in grafo.edges(data=True):
            if alvo[2]['produto'] == produto_alvo:
                return alvo[1]
        return None

    def calcular_fluxo(self, grafo, no_atual):
        valor_total = 0
        predecessores = list(grafo.predecessors(no_atual))
        
        for predecessor in predecessores:
            dados_da_aresta = grafo[predecessor][no_atual]
            tipo = dados_da_aresta['tipo_fluxo']
            
            if tipo == 'Entrada_Externa':
                valor_total += dados_da_aresta['quantidade']
            else:
                valor_do_passado = self.calcular_fluxo(grafo, predecessor)
                
                if tipo == 'Normal' or tipo == 'Co_Produto':
                    valor_total += valor_do_passado
                    
                elif tipo == 'Split':
                    total_produzido = 0 
                    for saida in grafo.out_edges(predecessor, data=True):
                        total_produzido += saida[2]['quantidade']
                        
                    if total_produzido > 0:
                        fracao = dados_da_aresta['quantidade'] / total_produzido
                        valor_total += valor_do_passado * fracao

        return valor_total

calculador_de_emergia = CalculadoraEmergetica()