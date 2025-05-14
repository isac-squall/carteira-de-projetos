import streamlit as st
import webbrowser

def run():
    # Função para mostrar o conteúdo da página de Contato
    st.subheader("Entre em Contato")
    st.write(
        """
        ✅Estou sempre aberto a novas oportunidades e colaborações. Se você tiver alguma dúvida ou quiser discutir um projeto, não hesite em entrar em contato!
        """
    )
    st.write(
        """
        ###Contato watsApp e email
        - **Email**:isac.cavalheiro@hotmail.com
        - **WhatsApp**: [Clique aqui para entrar em contato](https://api.whatsapp.com/send?phone=5511969527161&text=Olá!%20Gostaria%20de%20saber%20mais%20sobre%20seus%20serviços.)
        """
    )