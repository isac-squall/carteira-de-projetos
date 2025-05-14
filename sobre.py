import streamlit as st
from PIL import Image

def run():
    # Título da página
    st.subheader("Sobre Mim")
    st.write(
        """
        Olá! Meu nome é Isac Cavalheiro e sou um desenvolvedor de software apaixonado por tecnologia e inovação. Tenho experiência em diversas áreas de desenvolvimento, incluindo aplicativos web, automação de processos e análise de dados.
        """
    )
    st.write(
        """
        ✅ Estou sempre buscando aprender novas tecnologias e aprimorar minhas habilidades. Acredito que a colaboração e o compartilhamento de conhecimento são fundamentais para o crescimento profissional.
        """
    )
    st.write(
        """
        Este projeto é uma aplicação web desenvolvida com Streamlit, que tem como objetivo apresentar meu portfólio e compartilhar alguns dos meus projetos mais relevantes. Aqui você encontrará informações sobre minhas habilidades, experiências e projetos em que trabalhei.
        """
    )
    # Carregar a imagem 'dev.jpeg'
    try:
        imagem = Image.open("imagens/dev.jpeg")
        st.image(imagem, caption="Isac Cavalheiro", use_container_width=True)
    except FileNotFoundError:
        st.error("A imagem 'dev.jpeg' não foi encontrada na pasta 'imagens'. Verifique o caminho e tente novamente.")