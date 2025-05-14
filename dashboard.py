import streamlit as st
from PIL import Image

def run():
    """Exibe o conteúdo da página de Dashboard"""
    # Função para mostrar o conteúdo da página de Dashboard
    st.subheader("Dashboard que fiz com Power BI e Python")

    st.write(
        """
        ✅ Aqui está um exemplo de um dashboard interativo que você pode criar com Python e Streamlit. 
        Ele permite visualizar e analisar dados de forma dinâmica.
        """
    )

    # Carregar a imagem 'dashpower.png'
    try:
        imagem = Image.open("imagens/dashpower.png")
        # Exibir a imagem no Streamlit
        st.image(imagem, caption="Dashboard Power BI", use_container_width=True)
    except FileNotFoundError:
        st.error("A imagem 'dashpower.png' não foi encontrada na pasta 'imagens'. Verifique o caminho e tente novamente.")

    # Carregar a imagem 'dashstream.png'
    try:
        imagem = Image.open("imagens/dashstream.png")
        # Exibir a imagem no Streamlit
        st.image(imagem, caption="Dashboard Streamlit", use_container_width=True)
    except FileNotFoundError:
        st.error("A imagem 'dashstream.png' não foi encontrada na pasta 'imagens'. Verifique o caminho e tente novamente.")

