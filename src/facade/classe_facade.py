from database.gerenciador_bd import gerenciador
from models.modelador_de_rede import modelador
from core.calculadora import calculador_de_emergia
import math

class ScaleFacade:
    def __init__(self):
        self.gerenciador = gerenciador
        self.modelador = modelador
        self.calculadora = calculador_de_emergia

    def salvar_arquivo(self, arquivo_csv):
        df = self.gerenciador.ler_arquivo_do_usuario(arquivo_csv)
        self.gerenciador.enviar_registros_para_sqlite(df)

    def excluir_arquivo(self):
        self.gerenciador.remover_registros()

    def buscar_registros(self, nome_do_produto):
        df = self.gerenciador.select_query(nome_do_produto)

        if df is None or df.empty:
            return None
        
        grafo = self.modelador.construir_grafo(df)
        return grafo
    
    def calculo_emergetico(self, grafo, produto):
        self.calculadora.cache.clear()
        no = self.calculadora.verificar_no_atual(grafo, produto)
        return self.calculadora.calcular_fluxo(grafo, no)
    
    def formatar_total_emergia(self, emergia_total):
        expoente = int(math.floor(math.log10(emergia_total)))
        mantissa = emergia_total / (10 ** expoente)
        return f"{mantissa:.2f} × 10^{expoente} seJ"
    
facade = ScaleFacade()