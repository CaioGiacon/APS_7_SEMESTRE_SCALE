import streamlit as st
import networkx as nx
import pandas as pd
from facade.classe_facade import facade
from grafico.visualizacao_fluxo import visualizador 

st.set_page_config(page_title='EmerGraph - S.C.A.L.E', page_icon='⚡', layout='wide')

@st.cache_resource
def iniciar_sessao():
    return facade

app = iniciar_sessao()

st.title('⚡ EmerGraph - S.C.A.L.E')
st.caption('Software for Emergy Algebra Calculations')
st.write('---') 

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

    st.dataframe(df_exemplo, use_container_width=True, hide_index=True)
    st.caption('O arquivo csv deve seguir estritamente essa formatação.')

st.write('---') 

with st.expander('Envie o arquivo csv', expanded=True):
    arquivo_do_usuario = st.file_uploader('Carregue o seu arquivo', type=['csv'])
    st.markdown('O banco de dados já está carregado, mas fique a vontade para incluir o seu próprio arquivo devidamente formatado.')

if arquivo_do_usuario:
    if st.button('Transferir o arquivo para o Banco de Dados'):
        with st.status('Iniciando o processamento...', expanded=True) as status:
            app.salvar_arquivo(arquivo_do_usuario)
            status.update(label='Transferência concluída!', state='complete', expanded=False) 

with st.sidebar:
    st.header('Sobre o EmerGraph')
    st.write('''
    O **EmerGraph - S.C.A.L.E** é um protótipo focado em 
    automatizar e facilitar cálculos avançados de álgebra emergética. 
    
    A ferramenta utiliza Python, SQLite e Streamlit para otimizar a manipulação de 
    dados complexos.
    ''')

st.write('---') 
st.subheader('🔍 PROCURAR PRODUTO')

nome_produto = st.text_input('Digite o nome do produto para consulta:')

if nome_produto:
    grafo_resultado = app.buscar_registros(nome_produto)
    
    if grafo_resultado is not None and len(grafo_resultado.nodes) > 0:
        st.success(f'Rede do produto "{nome_produto}" montada com sucesso!')
        
        with st.expander('Ver detalhes técnicos (JSON/Estrutura)'):
            dicionario_interno = nx.to_dict_of_dicts(grafo_resultado)
            st.json(dicionario_interno)

        st.subheader('Visualização da Topologia da Rede')
        figura_grafo = app.plotar_grafico(grafo_resultado, titulo=f'Estrutura de Fluxos: {nome_produto}') 
        st.plotly_chart(figura_grafo, use_container_width=True)
        
        st.write('---')
    
        st.subheader('Métricas')
        valor_emergetico = app.calculo_emergetico(grafo_resultado, nome_produto)
        total = app.formatar_total_emergia(valor_emergetico)
        st.metric(label='Emergia Total', value=f'{total}')

        st.write('---')    
    else:
        st.error('Produto não encontrado ou rede vazia. Verifique o nome digitado.')