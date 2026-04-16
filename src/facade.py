from database.gerenciador_bd import gerenciador
from models.modelador_de_rede import modelador

class ScaleFacade:
    def __init__(self):
        self.gerenciador = gerenciador
        self.modelador = modelador

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