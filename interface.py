import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from buscar_cifras import buscar_arquivos
from pathlib import Path

# Configuração da página do Streamlit
st.set_page_config(page_title="---", layout="wide")

# 1. Carrega os tickers do seu arquivo CSV
@st.cache_data # Cache para carregar o arquivo rápido sem reprocessar a cada clique
def carregar_musicas():
    dados = buscar_arquivos(r"cifras") 
    nomes_sem_pdf = [nome.removesuffix(".pdf") for nome in dados]
    return sorted(nomes_sem_pdf, key=str.lower)
  
try:
    lista_musicas = carregar_musicas()
    musica_selecionada = st.selectbox("Escolha a música:", lista_musicas)
    musica_selecionada_tipo = musica_selecionada+".pdf"
    pasta_cifras = Path(r"cifras")
    caminho = pasta_cifras / musica_selecionada_tipo
    print(caminho)
    
    if musica_selecionada:
        st.subheader(f"{musica_selecionada}", text_alignment="justify")
        pdf_viewer(input=caminho, height=800)
 
except FileNotFoundError:
    st.error("Cifra não econtrada, tente outro nome!")