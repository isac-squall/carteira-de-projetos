import streamlit as st

def run():
    """Exibe o conteúdo da página de Vídeos"""
    # Título da página
    st.subheader("Meus Vídeos no YouTube para Descontrair")
    st.write(
        """
        ✅ Aqui estão alguns dos meus vídeos disponíveis no YouTube. 
        Sinta-se à vontade para explorar e deixar seu feedback!
        """
    )

    # Link para o canal do YouTube
    st.markdown(
        """
        - **[Canal do YouTube](https://www.youtube.com/@isaccavalheiro7228)**: Confira meus vídeos e inscreva-se no canal!
        """,
        unsafe_allow_html=True,
    )