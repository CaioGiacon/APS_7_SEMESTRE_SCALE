import streamlit as st
from database.gerenciador_bd import GerenciadorDeBanco

st.title('SCALE - Software para Cálculo Emergéticos')
gerenciador = GerenciadorDeBanco()


with st.expander('Envie o arquivo csv'):
    arquivo_do_usuario = st.file_uploader('Carregue o seu arquivo', type=['csv'])

if arquivo_do_usuario:
    if st.button('Transferir o arquivo para o Banco de Dados'):
        with st.status('Iniciando o processamento...', expanded=True) as status:
            
            arquivo = gerenciador.ler_arquivo_do_usuario(arquivo_do_usuario)
            dataframe = gerenciador.enviar_registros_para_sqlite(arquivo)
            status.update(label="Transferência concluída!", state="complete", expanded=False)
        st.success('Dados inseridos no Banco com sucesso✅.')

if st.button('Remover registros'):
    status_banco = gerenciador.remover_registro()
    st.success('✅ Banco limpo!')