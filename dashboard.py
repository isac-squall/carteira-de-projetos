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

    # Caminhos das imagens
    dashpower_path = "imagens/dashpower.png"
    dashstream_path = "imagens/dashstream.png"

    # Exibir dashpower.png
    if os.path.exists(dashpower_path):
        imagem = Image.open(dashpower_path)
        st.image(imagem, caption="Dashboard Power BI", use_container_width=True)
    else:
        st.warning("A imagem 'dashpower.png' não foi encontrada na pasta 'imagens'. Verifique o caminho e tente novamente.")

    # Exibir dashstream.png
    if os.path.exists(dashstream_path):
        imagem = Image.open(dashstream_path)
        st.image(imagem, caption="Dashboard Streamlit", use_container_width=True)
    else:
        st.warning("A imagem 'dashstream.png' não foi encontrada na pasta 'imagens'. Verifique o caminho e tente novamente.")

