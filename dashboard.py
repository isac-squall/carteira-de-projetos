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

<<<<<<< HEAD
    # Carregar a imagem 'dashpower.png'
    try:
        imagem = Image.open("dashpower.png")
        # Exibir a imagem no Streamlit
        st.image(imagem, caption="Dashboard Power BI", use_container_width=True)
    except FileNotFoundError:
        st.error("A imagem 'dashpower.png' não foi encontrada. Verifique o caminho e tente novamente.")

    # Carregar a imagem 'dashstream.png'
    try:
        imagem = Image.open("dashstream.png")
        # Exibir a imagem no Streamlit
        st.image(imagem, caption="Dashboard Streamlit", use_container_width=True)
    except FileNotFoundError:
        st.error("A imagem 'dashstream.png' não foi encontrada. Verifique o caminho e tente novamente.")

=======
    imagem = Image.open("Imagens/dashstream.png")
    st.image(imagem, caption="Dashboard Interativo", use_column_width=True)
    imagem = Image.open("Imagens/dashpower.png")
    st.image(imagem, caption="Dashboard Interativo", use_column_width=True)
>>>>>>> 71990449c58f942b05dd48591bcb7343d02a6cdf
