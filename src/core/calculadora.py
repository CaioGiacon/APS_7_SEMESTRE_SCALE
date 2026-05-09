class CalculadoraEmergetica:
    def __init__(self):
        self.cache = {}

    def verificar_no_atual(self, grafo, produto_alvo):
        for alvo in grafo.edges(data=True):
            if alvo[2]['produto'] == produto_alvo:
                return alvo[1]
        return None

    def calcular_fluxo(self, grafo, no_atual, no_visitado=None):
        if no_visitado is None:
            no_visitado = set()
        
        if no_atual in no_visitado:
            return 0
        
        if no_atual in self.cache:
            return self.cache[no_atual]
    
        no_visitado.add(no_atual)
        valor_total = 0
        
        for predecessor in list(grafo.predecessors(no_atual)):
            dados_da_aresta = grafo[predecessor][no_atual]
            tipo = dados_da_aresta['tipo_fluxo']
            quantidade = dados_da_aresta['quantidade']
            transformidade = dados_da_aresta.get('transformidade', 1)
            
            if tipo == 'Entrada_Externa':
                valor_total += quantidade * transformidade
            else:
                valor_do_passado = self.calcular_fluxo(grafo, predecessor, no_visitado.copy())
                
                if tipo == 'Normal' or tipo == 'Co_Produto':
                    valor_total += valor_do_passado * transformidade
                    
                elif tipo == 'Split':
                    total_produzido = sum(
                        saida[2]['quantidade']
                        for saida in grafo.out_edges(predecessor, data=True)
                    )

                    fracao = quantidade / total_produzido

                    valor_total += valor_do_passado * fracao * transformidade
        self.cache[no_atual] = valor_total
        return valor_total

calculador_de_emergia = CalculadoraEmergetica()