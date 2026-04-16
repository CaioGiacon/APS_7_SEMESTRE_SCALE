# SCALE (Software for Emergy Algebra Calculations)

> ⚠️ **Status do Projeto:** 🏗️ Em Construção / Desenvolvimento.
> Este software é um protótipo em fase de implementação e refinamento de funcionalidades.

O **SCALE** é um software dedicado à automação e facilitação de cálculos complexos dentro da **Álgebra Emergética**. O objetivo central é transformar modelos matemáticos e fluxos sistêmicos em uma ferramenta digital acessível, garantindo rigor científico e eficiência no processamento de dados ambientais e econômicos.

## 🚀 Tecnologias e Bibliotecas

As escolhas técnicas buscam o equilíbrio entre a robustez no tratamento de dados e a agilidade na entrega de uma interface interativa:

* **Python:** Linguagem principal utilizada para toda a lógica de negócios e processamento.
* **Streamlit:** Utilizado para a construção da interface web, permitindo visualização de dados em tempo real.
* **SQLite:** Banco de dados relacional leve para a persistência e gerenciamento local dos dados inseridos.
* **Pandas:** Biblioteca fundamental para a manipulação, estruturação e tratamento de tabelas de dados de entrada e saída.
* **NetworkX:** Utilizada para a modelagem dos fluxos de energia através de **grafos**, essencial para analisar as interconexões e o cálculo de transformidades no sistema.

## 🏗️ Arquitetura e Decisões de Projeto

A arquitetura do SCALE foi projetada para atender às exigências de um ambiente acadêmico e profissional, onde a transparência dos cálculos e a facilidade de manutenção são cruciais. O desenvolvimento é inteiramente baseado nos princípios de **Programação Orientada a Objetos (POO)**.

### Fundamentos da Escolha Arquitetural

A separação do sistema em camadas de responsabilidade visa o **desacoplamento**, permitindo que o motor de cálculo evolua independentemente da interface. As decisões principais incluem:

1.  **Padrão Facade (Fachada):**
    - **Motivação:** A Álgebra Emergética possui múltiplos processos internos (grafos, matrizes, persistência). A *Facade* centraliza essas complexidades em uma interface única. Isso permite que o `Streamlit` (camada de apresentação) solicite operações complexas sem precisar conhecer os detalhes internos do motor de cálculo.
2.  **Database Manager (Gerenciador de Banco de Dados):**
    - **Motivação:** Seguindo o princípio de responsabilidade única, toda a comunicação com o SQLite é isolada em uma classe gestora. Isso protege a integridade dos dados e facilita a migração ou expansão do banco no futuro.
3.  **Abstração e POO:**
    - O uso de classes para representar componentes do sistema garante que o código seja modular. Isso facilita a auditoria dos cálculos (importante para validação acadêmica) e a reutilização de componentes em diferentes módulos do software.

## ⚙️ Como Executar o Projeto (Ambiente de Desenvolvimento)

*Nota: Como o projeto está em construção, certifique-se de estar na branch principal.*

### Instalação

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/seu-usuario/scale.git](https://github.com/seu-usuario/scale.git)
    cd scale
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

Para rodar o protótipo atual:
```bash
streamlit run app.py
```

## 👨‍💻 Autor
Caio Giacon
