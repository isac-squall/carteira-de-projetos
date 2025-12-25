import streamlit as st
import importlib
from PIL import Image
import webbrowser

# Configuração da página
st.set_page_config(
    page_title="Portfólio - Isac.Cavalheiro",
    page_icon=":globe_with_meridians:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_css():
    """Carrega todos os estilos CSS"""
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --primary-color: #1a365d;
                --secondary-color: #2d547d;
                --accent-color: #38bdf8;
                --text-light: #f8fafc;
                --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }

            .project-card {
                background: white;
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: var(--shadow);
                transition: all 0.3s ease;
                border: 1px solid rgba(0, 0, 0, 0.1);
            }

            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }

            .experience-item {
                padding: 1.5rem;
                background: white;
                border-radius: 10px;
                box-shadow: var(--shadow);
                margin-bottom: 1.5rem;
                transition: all 0.3s ease;
            }

            .experience-item:hover {
                transform: translateY(-3px);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_pages(page):
    """Carrega o módulo correspondente à página selecionada"""
    modules = {
        "Início": "inicio",
        "Projetos": "projetos",
        "Vídeos": "videos",
        "Dashboard": "dashboard",
        "Contato": "contato",
        "Sobre": "sobre",
    }
    module_name = modules.get(page)
    if module_name:
        try:
            module = importlib.import_module(module_name)
            # Verifica se o módulo tem a função run()
            if hasattr(module, "run"):
                module.run()
            else:
                st.write("O módulo selecionado não possui a função 'run()'.")
        except ModuleNotFoundError:
            st.write(f"Erro: O módulo '{module_name}' não foi encontrado.")
    else:
        st.write("Página não encontrada.")


def main():
    # Carrega o CSS
    load_css()

    # Cria a barra lateral
    with st.sidebar:
        # Imagem e título
        st.image("Isac.jpg", width=200)
        st.title("Isac Cavalheiro")

        # Redes sociais
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Redes Sociais</h3>
                <a href="https://www.linkedin.com/in/isac-cavalheiro" target="_blank" style="margin: 0 10px;">
                    <i class="fab fa-linkedin" style="font-size: 24px; color: #0077b5;"></i>
                </a>
                <a href="https://github.com/isac-squall" target="_blank" style="margin: 0 10px;">
                    <i class="fab fa-github" style="font-size: 24px; color: #333;"></i>
                </a>
                <a href="https://www.instagram.com/isacwebdesign/" target="_blank" style="margin: 0 10px;">
                    <i class="fab fa-instagram" style="font-size: 24px; color: #e4405f;"></i>
                </a>
                <a href="https://www.facebook.com/isac.degoescavalheiro" target="_blank" style="margin: 0 10px;">
                    <i class="fab fa-facebook" style="font-size: 24px; color: #1877f2;"></i>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Informações de contato
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Contato</h3>
                <p><strong>Email:</strong> isac.cavalheiro@hotmail.com</p>
                <p><strong>📞 Telefone:</strong> (11) 9 6952-7161</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Menu de navegação (agora acima das informações profissionais)
        page = st.selectbox(
            label="Navegação",
            options=["Início", "Projetos", "Vídeos", "Dashboard", "Contato", "Sobre"],
            index=0,
        )

        # Informações profissionais
        st.markdown(
            """
            <div style="text-align: center;">
                <h2>👉 Analista de Sistema</h2>
                <p><strong>🎓Graduação:</strong> Gestão de Tecnologia da Informação (2019)</p>
                <p><strong>Experiência:</strong></p>
                <ul style="list-style-type: none; padding: 0;">
                    <li>Assistente de TI na Horus Risk Soluçõoes em Gestão de Risco LTDA 🗓️ 2026</li>
                    <li>Analista de Suporte Jr na C8 Sistemas ERP 🗓️ 2025</li>
                    <li>Analista de Implementação ERP na Simpledot 🗓️ 2024</li>
                </ul>
                <p><strong>📍 Localização:</strong> Osasco, São Paulo, Brasil</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Mostra a página selecionada
    show_pages(page)

    # Adiciona um rodapé
    st.markdown(
        """
        <footer style="text-align: center; padding: 1rem; background-color: #f1f1f1;">
            <p>© 2025 Isac Cavalheiro. Todos os direitos reservados.</p>
        </footer>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
