import streamlit as st
from facade import ScaleFacade

@st.cache_resource
def iniciar_sessao():
    return ScaleFacade()

app = iniciar_sessao()

with st.sidebar:
    st.header("Sobre o S.C.A.L.E")
    st.write("""
    O **S.C.A.L.E (Software for Emergy Algebra Calculations)** é um protótipo focado em 
    automatizar e facilitar cálculos avançados de álgebra emergética. 
    
    A ferramenta utiliza Python, SQLite e Streamlit para otimizar a manipulação de 
    dados complexos, entregando uma solução tecnológica estruturada e eficiente.
    """)
st.title('S.C.A.L.E - Emergy Algebra',)

with st.expander('Envie o arquivo csv', expanded=True):
    arquivo_do_usuario = st.file_uploader('Carregue o seu arquivo', type=['csv'])

if arquivo_do_usuario:
    if st.button('Transferir o arquivo para o Banco de Dados'):
        with st.status('Iniciando o processamento...', expanded=True) as status:
            app.salvar_arquivo(arquivo_do_usuario)
            status.update(label="Transferência concluída!", state="complete", expanded=False) 

st.write("---") 
st.subheader("PROCURAR PRODUTO")

nome_produto = st.text_input("Digite o nome do produto para consulta:").title()

if nome_produto:
    grafo_resultado = app.buscar_registros(nome_produto)
    
    if grafo_resultado is not None:
        st.success(f"Rede do produto '{nome_produto}' montada com sucesso!")
        qtd_nos = grafo_resultado.number_of_nodes()
        qtd_arestas = grafo_resultado.number_of_edges()     
        st.info(f"O sistema identificou {qtd_nos} processos e {qtd_arestas} conexões.")
    else:
        st.error("Produto não encontrado no banco de dados. Tente outro nome.")