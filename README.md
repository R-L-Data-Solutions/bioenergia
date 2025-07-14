# 🌿 Painel do Produtor - Belém Bioenergia Brasil

Dashboard interativo desenvolvido com [Streamlit](https://streamlit.io) para acompanhamento das etapas do crédito rural dos produtores da **Belém Bioenergia Brasil**.

## 📌 Objetivo

Acompanhar, filtrar e visualizar dados em tempo real sobre o andamento das cédulas de crédito por produtor, facilitando a comunicação entre gestores e equipe técnica.

## 🖥️ Funcionalidades

- ✅ Filtros por Nome, CPF, Município e Agência
- 🧭 Status das etapas centralizadas (como Laudo, Cartório, Recurso Liberado)
- 📊 Tabela interativa com exportação para CSV
- 🔗 Integração com [Google Sheets](https://docs.google.com/spreadsheets/)
- 📁 Upload futuro de PDFs (em desenvolvimento)

## 🏗️ Tecnologias Utilizadas

- Python 3.9+
- Streamlit
- Pandas
- gspread (Google Sheets API)
- OAuth2 / Google Service Account

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/R-L-Data-Solutions/produtor-dashboard.git
cd produtor-dashboard

2. Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
3. Instale as dependências:

pip install -r requirements.txt
4. Execute a aplicação:

streamlit run painel_produtor_streamlit.py
📝 Acesso ao Google Sheets
Caso use dados online:

Crie um arquivo credentials.json com uma conta de serviço do Google.

Compartilhe a planilha com o e-mail gerado no Google Cloud.

Atualize o script com o ID da planilha.

📎 Exemplo
Acesse a aplicação publicada aqui:

📍 https://nome-do-projeto.streamlit.app

👥 Sobre a R&L Data Solutions
Soluções personalizadas em dados, automações e inteligência para empresas que querem crescer com tecnologia.
