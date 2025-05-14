import streamlit as st
from PIL import Image
import os

def run():
    """Exibe o conteúdo da página de Dashboard"""
    st.subheader("Dashboard que fiz com Power BI e Python")

    st.write(
        """
        ✅ Aqui está um exemplo de um dashboard interativo que você pode criar com Python e Streamlit. 
        Ele permite visualizar e analisar dados de forma dinâmica.
        """
    )

    imagem = Image.open("Imagens/dashstream.png")
    st.image(imagem, caption="Dashboard Interativo", use_column_width=True)
    imagem = Image.open("Imagens/dashpower.png")
    st.image(imagem, caption="Dashboard Interativo", use_column_width=True)
