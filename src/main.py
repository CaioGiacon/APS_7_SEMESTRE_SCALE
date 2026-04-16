import streamlit as st
from facade import ScaleFacade

@st.cache_resource
def iniciar_sessao():
    return ScaleFacade()

app = iniciar_sessao()

st.title('S.C.A.L.E - Emergy Algebra')

with st.expander('Envie o arquivo csv'):
    arquivo_do_usuario = st.file_uploader('Carregue o seu arquivo', type=['csv'])

if arquivo_do_usuario:
    if st.button('Transferir o arquivo para o Banco de Dados'):
        with st.status('Iniciando o processamento...', expanded=True) as status:
            app.salvar_arquivo(arquivo_do_usuario)
            status.update(label="Transferência concluída!", state="complete", expanded=False) 

if st.button('Remover registros'):
    status_banco = app.excluir_arquivo()
    st.success('✅ Banco limpo!')


