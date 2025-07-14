import streamlit as st
import pandas as pd
import os
from PIL import Image
import time


st.set_page_config(page_title="Painel do Produtor", layout="wide")

# Carrega o logo
logo = Image.open("bioenergia_logo.jpg")

# Cria layout com duas colunas: logo + título
col1, col2 = st.columns([1, 8])
with col1:
    st.image(logo, width=80)  # Pode ajustar o tamanho aqui
with col2:
    st.markdown("## Painel do Produtor - Belém Bioenergia Brasil")


st.markdown("""
Sistema de acompanhamento das etapas de liberação de crédito rural.  
Filtre abaixo pelo nome do produtor, CPF, município ou agência para visualizar o status atual.
""")

@st.cache_data(ttl=60)
def carregar_dados():
    url = "https://docs.google.com/spreadsheets/d/1RxiB6hYWG41Kycbw4yGprncC9P91BSV8y_8-0OEnosQ/export?format=csv"
    return pd.read_csv(url)

    # try:
    #     # 🟢 Modo local (CSV baixado do SharePoint)
    #     return pd.read_csv("Cédula_de_Crédito_2025(CÉDULAS).csv", encoding='latin1')
        
    #     # 🔵 Caso queira usar o Google Sheets depois, descomente a linha abaixo:
    #     # return pd.read_csv(url)
    # except Exception as e:
    #     st.error(f"Erro ao carregar os dados: {e}")
    #     return pd.DataFrame()

df = carregar_dados()
df = df.dropna(subset=["AGÊNCIA"])


if df.empty:
    st.warning("Nenhum dado carregado. Verifique o arquivo local ou o link da nuvem.")
    st.stop()

# 🎯 Filtros
st.sidebar.header("🔎 Filtros")
nome_produtor = st.sidebar.text_input("Nome do Produtor")
cpf = st.sidebar.text_input("CPF")
#agencia = st.sidebar.text_input("Agência")
# Garante que todos os valores estejam formatados corretamente
df["AGÊNCIA"] = df["AGÊNCIA"].astype(str).str.strip().str.upper()

# Pega valores únicos (sem nulos), ordenados
agencias_unicas = sorted(df["AGÊNCIA"].dropna().unique())
agencia = st.sidebar.selectbox("Agência", ["Todas"] + agencias_unicas)

# Aplica filtro se diferente de "Todas"
if agencia != "Todas":
    df = df[df["AGÊNCIA"] == agencia]

municipio = st.sidebar.text_input("Município")
status_busca = st.sidebar.selectbox("Status (em qualquer etapa)", ["Todos", "DESISTIU", "DILIGÊNCIA", "ENVIADO", "LIBERADO", "NÃO ENVIADO"])

# 🔍 Aplicando filtros
if nome_produtor:
    df = df[df["PRODUTOR"].str.contains(nome_produtor, case=False, na=False)]
if cpf:
    df = df[df["CPF"].astype(str).str.contains(cpf, na=False)]
if agencia != "Todas":
    df = df[df["AGÊNCIA"] == agencia]
# if agencia:
#     df = df[df["AGÊNCIA"].astype(str).str.contains(agencia, na=False)]
if municipio:
    df = df[df["MUNICÍPIO"].str.contains(municipio, case=False, na=False)]
if status_busca != "Todos":
    colunas_status = ["PRODUTOR.1", "DIRETORIA", "CARTÓRIO", "RECURSO LIBERADO", "DATA DE ENVIO AO BANCO"]

    df = df[
        df[colunas_status].apply(
            lambda row: any(str(cell).strip().lower() == status_busca.strip().lower() for cell in row.values),
            axis=1
        )
    ]


# 📋 Exibe tabela principal
st.markdown("### 📊 Tabela de Acompanhamento")
colunas_exibir = [
    "PRODUTOR", "CPF", "AGÊNCIA", "MUNICÍPIO",
    "DATA DE RECEBIMENTO", "PRODUTOR.1", "DIRETORIA", "CARTÓRIO",
    "RECURSO LIBERADO", "DATA DE ENVIO AO BANCO",
    "HECTARE", "QUANTIDADE DE MUDAS", "VALOR MUDAS",
    "ENDEREÇO", "POLO", "LAUDO - 1", "LAUDO - 2", "LAUDO - 3"
]
colunas_existentes = [col for col in colunas_exibir if col in df.columns]
st.dataframe(df[colunas_existentes], use_container_width=True)

# 💾 Exportar CSV
st.download_button(
    label="⬇️ Exportar CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="painel_produtores_filtrado.csv",
    mime="text/csv"
)

# Rodapé com marca e citação
st.markdown(
    """
    <hr style="margin-top: 50px; margin-bottom: 10px;"/>
    <div style="text-align: center; font-size: 12px; color: gray;">
        R&L Data Solutions | <i>Habacuque 2:2 - "Escreve a visão, grava-a sobre tábuas, para que a possa ler até quem passa correndo."</i>
    </div>
    """,
    unsafe_allow_html=True
)
