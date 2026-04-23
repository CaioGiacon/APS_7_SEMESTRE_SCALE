# ⚡ EmerGraph - S.C.A.L.E
**Software for Emergy Algebra Calculations**

> ⚠️ **Status do Projeto:** 🏗️ Finalizado / Aguardando Avaliação.
> Importante frisar que o EmerGraph - S.C.A.L.E é um protótipo.

O **EmerGraph - S.C.A.L.E** (Software for Emergy Algebra Calculations) é uma ferramenta desenvolvida para a modelagem, automação e análise de sistemas através da **Álgebra Emergética**. Unindo os conceitos de fluxos de energia à teoria de grafos, o software transforma cálculos matemáticos complexos em uma estrutura digital clara, facilitando a contabilidade ambiental e a avaliação da sustentabilidade sistêmica.

## ✨ Funcionalidades Principais

* **Importação Dinâmica de Dados:** Leitura de arquivos CSV fornecidos pelo usuário, com tratamento robusto de erros (codificação, estrutura, permissões).
* **Persistência Relacional:** Armazenamento automatizado e centralizado dos registros de fluxo utilizando banco de dados SQLite.
* **Modelagem Topológica:** Construção de redes em formato de grafos direcionados, rastreando origem, destino, tipo de fluxo e transformidade dos produtos.
* **Motor de Cálculo Avançado:**
  * Processamento recursivo dos valores emergéticos na rede.
  * Sistema de *cache* integrado para otimização de varreduras em nós já calculados.
  * Detecção de ciclos (loopbacks) estruturais para prevenir falhas de cálculo.
  * Suporte a regras de negócio baseadas no tipo de fluxo (`Normal`, `Entrada_Externa`, `Co_Produto`, `Split`).
* **Visualização Interativa:** Geração de diagramas tipo Sankey para análise visual clara do balanço de energia e massa da rede.
* **Formatação Científica:** Apresentação inteligente de resultados em notação científica para grandezas emergéticas elevadas (seJ).

## 🚀 Tecnologias e Bibliotecas

A stack tecnológica foi selecionada para suportar o processamento de dados e a representação visual de redes complexas:

* **Linguagem:** Python 3.12.10
* **Interface Web:** Streamlit 
* **Lógica de Redes:** NetworkX 
* **Gráficos e Visualização:** Plotly 
* **Estrutura de Dados:** Pandas 
* **Persistência Local:** SQLite
* **Cobertura de Testes:** Pytest 
* **Containerização:** Docker

## 🏗️ Arquitetura e Decisões de Projeto

O sistema é estruturado sob os princípios de **Programação Orientada a Objetos (POO)**, garantindo modularidade e permitindo que novos métodos de álgebra sejam adicionados sem comprometer a estabilidade do núcleo:

1. **Padrão Facade (Fachada):**
   A classe `ScaleFacade` atua como um ponto único de entrada orquestrando o gerenciador de banco de dados, o modelador e a calculadora. Isso simplifica a comunicação com o Streamlit, mantendo a interface isolada da lógica de negócios pesada.
2. **Database Manager (Gerenciador de Banco):**
   Centraliza todas as operações SQL, incluindo o uso de *Common Table Expressions (CTEs) recursivas* para montagem ágil das sub-redes dos grafos.
3. **Modelagem por Grafos (NetworkX):**
   Representar fluxos como grafos direcionados permite varrer precursores sistematicamente, identificar gargalos energéticos e aplicar validações matemáticas (como checagem DAG - Directed Acyclic Graph) exclusivas à teoria de emergia.

## ⚙️ Como Executar o Projeto

A aplicação foi conteinerizada com Docker para garantir que rode de forma idêntica em qualquer máquina, dispensando a instalação e configuração manual de dependências.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/CaioGiacon/APS_7_SEMESTRE_SCALE.git](https://github.com/CaioGiacon/APS_7_SEMESTRE_SCALE.git)
   cd APS_7_SEMESTRE_SCALE
   ```

2. **Construa a Imagem do Docker:**
    ```bash
    docker build -t scale-app .
    ```

3. **Inicialize o container (atribuindo um nome de sua escolha):**
    ```bash
    docker run --name NOME_DO_SEU_CONTEINER -p 8501:8501 scale-app
    ```
    Substitua NOME_DO_SEU_CONTEINER pelo nome que desejar. A aplicação estará disponível em http://localhost:8501.

## 🧪 Testes Unitários
O protótipo acompanha uma suíte de testes unitários desenvolvida em Pytest para atestar a precisão das engrenagens matemáticas (como a validação do cálculo de Etanol e a garantia de que as redes geradas são grafos acíclicos direcionados).

Como a aplicação está conteinerizada, você pode rodar os testes de forma isolada sem precisar instalar dependências na sua máquina.

Passo a passo para rodar os testes via Docker:

    1. Certifique-se de que a imagem scale-app já foi construída (passo 2 da seção anterior).

    2. Execute o comando abaixo no seu terminal. Ele criará um container temporário apenas para rodar as validações:
    ```bash
    docker run --rm scale-app pytest
    ```
    (A flag --rm garante que este container de teste seja destruído automaticamente após a execução dos testes, mantendo seu ambiente limpo).

Alternativa (Para Desenvolvimento Local):
Caso queira desenvolver e testar fora do Docker:

    1. Crie e ative um ambiente virtual (python -m venv venv).

    2. Instale os requisitos: pip install -r requirements.txt.

    3. Rode o comando pytest na raiz do projeto.

## 👨‍💻 Autor
Caio Giacon