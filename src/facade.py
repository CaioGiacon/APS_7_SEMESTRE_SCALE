from database.gerenciador_bd import GerenciadorDeBanco

class ScaleFacade:
    def __init__(self):
        self.gerenciador = GerenciadorDeBanco()

    def salvar_arquivo(self, arquivo_csv):
        df = self.gerenciador.ler_arquivo_do_usuario(arquivo_csv)
        self.gerenciador.enviar_registros_para_sqlite(df)

    def excluir_arquivo(self):
        self.gerenciador.remover_registros()