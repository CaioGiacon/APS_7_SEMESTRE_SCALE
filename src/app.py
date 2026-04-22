import streamlit as st
from facade.classe_facade import facade
import networkx as nx
import pandas as pd

@st.cache_resource
def iniciar_sessao():
    return facade

app = iniciar_sessao()

st.title('⚡ EmerGraph - S.C.A.L.E', text_alignment='center')
st.write("---") 

with st.expander('Exemplo de formatação do arquivo (CSV ou Excel)'):
    st.markdown('O seu arquivo deve seguir o seguinte padrão de nomes nas colunas.')
    
    df_exemplo = pd.DataFrame({
        'id': [1, 2, 3],
        'origem': ['Sol', 'Fermentacao', 'Moagem'],
        'destino': ['Cana', 'Destilacao', 'Fermentacao'],
        'produto': ['Nutrientes', 'Etanol Bruto', 'Acucar'],
        'quantidade': [1000, 1200, 900],
        'tipo_fluxo': ['Co_Produto', 'Normal', 'Entrada_Externa'],
        'transformidade': [8, 5, 1]
    })

    st.dataframe(df_exemplo, width=True, hide_index=True)
    st.caption('Trata-se de um exemplo.')

st.write("---") 

with st.expander('Envie o arquivo csv', expanded=True):
    arquivo_do_usuario = st.file_uploader('Carregue o seu arquivo', type=['csv'])

if arquivo_do_usuario:
    if st.button('Transferir o arquivo para o Banco de Dados'):
        with st.status('Iniciando o processamento...', expanded=True) as status:
            app.salvar_arquivo(arquivo_do_usuario)
            status.update(label="Transferência concluída!", state="complete", expanded=False) 

with st.sidebar:
    st.header("Sobre o EmerGraph - S.C.A.L.E")
    st.write("""
    O ** EmerGraph - S.C.A.L.E (Software for Emergy Algebra Calculations)** é um protótipo focado em 
    automatizar e facilitar cálculos avançados de álgebra emergética. 
    
    A ferramenta utiliza Python, SQLite e Streamlit para otimizar a manipulação de 
    dados complexos, entregando uma solução tecnológica estruturada e eficiente.
    """)

st.set_page_config(page_title='EmerGraph - S.C.A.L.E', page_icon='⚡', layout='wide')

st.write("---") 
st.subheader("PROCURAR PRODUTO")

nome_produto = st.text_input("Digite o nome do produto para consulta:").title()

if nome_produto:
    grafo_resultado = app.buscar_registros(nome_produto)
    if grafo_resultado is not None:
        st.success(f"Rede do produto {nome_produto} montada com sucesso!")
        dicionario_interno = nx.to_dict_of_dicts(grafo_resultado)
        st.json(dicionario_interno)
        st.write('---') 
        
        valor_emergetico = app.calculo_emergetico(grafo_resultado, nome_produto)
        total = app.formatar_total_emergia(valor_emergetico)
        st.write(f'Valor Emergético Total do produto {nome_produto} é de: {total}')
    else:
        st.error("Produto não encontrado no banco de dados. Tente outro nome.")

