import streamlit as st
import importlib
import os

def run():
    # Função para mostrar o conteúdo da página de Projetos
    st.subheader("Meus Projetos no GitHub")
    st.write(
        """
        ✅Aqui estão alguns dos meus projetos disponíveis no GitHub. Sinta-se à vontade para explorar e contribuir!
      
        """

    )
    st.write(
        """
        ### Projetos em Destaque
         - **Certificação de Ingles A1 INICIANTE**:https://cert.efset.org/pt/5Pt2sK Uma certificação de inglês, Sua pontuação no EF SET indica que seu nível é A1 INICIANTE, de acordo com as diretrizes estabelecidas pelo Quadro Europeu Comum de Referência para Línguas (QECR).
        - **Gerenciador de Tarefas**:https://isac-squall-projeto-crud-todo-streamlit-appsrcapp-orfsng.streamlit.app/ Um sistema de gerenciamento de tarefas, desenvolvido com Python e SQLite3, que permite criar, editar e excluir tarefas, além de visualizar uma lista de tarefas existentes.
        - **Consumo de API-COM-PYTHON**:https://github.com/isac-squall/API-COM-PYTHON Uma aplicação que consome dados de uma API pública e os apresenta de forma organizada, utilizando Python e bibliotecas como Requests e Pandas.
        - **DASHBOARD Feito com Python**:https://isac-squall-analise-de-planilhas-excel-com-streaml-index-9wkhrm.streamlit.app/ Uma aplicação de dashboard interativa, desenvolvida com Streamlit, Pandas e Plotly, que permite visualizar e analisar dados de forma dinâmica.
        - **Site feito em HTML/CSS/JAVASCRIT**:https://site-dayanenail.vercel.app/ Um site de portfólio pessoal, desenvolvido com HTML, CSS e JavaScript, apresentando trabalho de design e desenvolvimento web.
        - **APP para calcular IMC EM Sqlite3/Python**:https://isac-squall-sistema-para-calcular-imc-streamlit-app-wph8pa.streamlit.app/ Um sistema de cálculo de IMC, desenvolvido com HTML, CSS e Python, utilizando SQLite3 para armazenamento de dados de usuários.
        - **Cadastro de Recruta HTML/CSS/javaScript**:https://github.com/isac-squall/Cadastro-de-recruta Uma aplicação simples de cadastro de recrutamento, desenvolvida com javaScript, HTML e CSS, permitindo o registro e gerenciamento de candidatos.
        - **Login em html/css/Sqlite3/Python**:https://github.com/isac-squall/Cadastro-de-recruta Um sistema de login simples, desenvolvido com HTML, CSS e Python, utilizando SQLite3 para armazenamento de dados de usuários.
        
        - **Automação de Processos**: Scripts em Python para automatizar tarefas repetitivas, como envio de e-mails e geração de relatórios.
        
        
        
        """
    )