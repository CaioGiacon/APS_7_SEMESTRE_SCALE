# EmerGraph - S.C.A.L.E

> ⚠️ **Status do Projeto:** 🏗️ Em Construção / Desenvolvimento.
> O EmerGraph é um protótipo em fase ativa de implementação e refinamento.

O **EmerGraph - S.C.A.L.E** (Software for Emergy Algebra Calculations) é uma ferramenta desenvolvida para a modelagem, automação e análise de sistemas através da **Álgebra Emergética**. Unindo os conceitos de fluxos de energia à teoria de grafos, o software transforma cálculos matemáticos complexos em uma estrutura digital clara, facilitando a contabilidade ambiental e a avaliação da sustentabilidade sistêmica.

## 🚀 Tecnologias e Bibliotecas

A stack tecnológica foi selecionada para suportar o processamento de dados e a representação visual de redes complexas:

* **Python:** Linguagem central para o desenvolvimento da lógica e algoritmos de cálculo.
* **Streamlit:** Interface web interativa que permite a manipulação de parâmetros e visualização de resultados em tempo real.
* **NetworkX:** Biblioteca chave para a modelagem dos fluxos sistêmicos como **grafos**, permitindo o cálculo de caminhos, transformidades e a análise da topologia da rede energética.
* **Pandas:** Utilizado para a estruturação eficiente de dados e tratamento das tabelas de entrada e saída.
* **SQLite:** Banco de dados relacional para persistência local segura das configurações e dados de álgebra.

## 🏗️ Arquitetura e Decisões de Projeto

O sistema é estruturado sob os princípios de **Programação Orientada a Objetos (POO)**, garantindo modularidade e permitindo que novos métodos de álgebra sejam adicionados sem comprometer a estabilidade do núcleo.

### Fundamentos da Escolha Arquitetural

A separação em camadas garante que a lógica científica (o motor de cálculo) esteja isolada da interface de usuário e do armazenamento:

1.  **Padrão Facade (Fachada):**
    - **Motivação:** Como a Álgebra Emergética envolve múltiplos processos internos, a *Facade* atua como um ponto único de entrada. Isso simplifica a comunicação com o `Streamlit`, mantendo o código da interface focado na experiência do usuário.
2.  **Database Manager (Gerenciador de Banco de Dados):**
    - **Motivação:** Centraliza todas as operações SQL, isolando a complexidade das consultas e garantindo que a lógica de persistência siga o princípio de responsabilidade única (SRP).
3.  **Modelagem por Grafos (NetworkX):**
    - **Motivação:** Representar os fluxos como grafos permite identificar ciclos de feedback e dependências estruturais que são fundamentais na teoria de emergia, indo além das capacidades de planilhas convencionais.

## ⚙️ Como Executar o Projeto (Ambiente de Desenvolvimento)

### Instalação

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/CaioGiacon/APS_7_SEMESTRE_SCALE.git](https://github.com/CaioGiacon/APS_7_SEMESTRE_SCALE.git)
    cd APS_7_SEMESTRE_SCALE
    ```

2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/macOS:
    source venv/bin/activate
    ```

3.  Instale as dependências:
    ```bash
    pip install streamlit pandas networkx
    ```

### Execução

Para iniciar o protótipo:
```bash
streamlit run app.py
```

## 👨‍💻 Autor
Caio Giacon
