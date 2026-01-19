import streamlit as st
from PIL import Image
import os

def run():
    """Exibe o conteúdo da página de Dashboard"""
    st.subheader("Dashboard que fiz com Power BI e Python")

    st.write(
        """
        ✅ Aqui está um exemplo de um dashboard interativo que desenvolvi com Python e Streamlit. 
        Permite visualizar e analisar dados de forma dinâmica.
        """
    )

    # Carregar a imagem 'dashpower.png'
    try:
        imagem = Image.open("dashpower.png")
        st.image(imagem, caption="Dashboard Power BI", use_container_width=True)
    except FileNotFoundError:
        st.error("A imagem 'dashpower.png' não foi encontrada. Verifique o caminho e tente novamente.")

    # Carregar a imagem 'dashstream.png'
    try:
        imagem = Image.open("dashstream.png")
        st.image(imagem, caption="Dashboard Streamlit", use_container_width=True)
    except FileNotFoundError:
        st.error("A imagem 'dashstream.png' não foi encontrada. Verifique o caminho e tente novamente.")
