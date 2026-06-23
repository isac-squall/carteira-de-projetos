import streamlit as st

def run() -> None:
    """Exibe o conteúdo da página inicial"""
    st.title("Bem-vindo ao meu portfólio!")

    st.markdown(
        """
        👉 Olá! Meu nome é **Isac Cavalheiro**, sou Analista e desenvolvedor Python para automação de processos em sistemas.  
        Neste portfólio, você encontrará informações sobre meus projetos, vídeos, dashboards, contato e um pouco sobre mim.

        ---
        ### 🎯 Experiência Profissional
        """,
        unsafe_allow_html=True,
    )

    # Experiência 1
    st.markdown(
        """
        <div class="experience-item">
            <h3>LUFT SOLUTIONS LOGISTIC LTDA</h3>
            <p><i class="fa-solid fa-briefcase"></i> Analista de Operações de II</p>
            <p><i class="fa-solid fa-calendar"></i> 02/03/2026 até 18/06/2026</p>
            <p><strong>Principais atividades:</strong></p>
            <ul>
                <li>Controle de pedidos de transporte via Power Apps.</li>
                <li>Acompanhamento da execução dos serviços das transportadoras e garantia do nível de serviço.</li>
                <li>Desenvolvimento e monitoramento de KPIs logísticos, criação de dashboards em Python.</li>
                <li>Automação de fluxos em Power Automate e apoio à melhoria contínua dos processos.</li>
                <li>Participação em reuniões com parceiros internos e externos para alinhamento operacional.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Experiência 2
    st.markdown(
        """
        <div class="experience-item">
            <h3>HORUS RISK SOLUÇÕES EM GESTÃO DE RISCO LTDA</h3>
            <p><i class="fa-solid fa-briefcase"></i> Assistente de TI</p>
            <p><i class="fa-solid fa-calendar"></i> 11/2025 até 27/02/2026</p>
            <p><strong>Principais atividades:</strong></p>
            <ul>
                <li>Suporte completo aos equipamentos e infraestrutura de TI do cliente.</li>
                <li>Instalação, configuração e manutenção de computadores, impressoras e cabeamento de rede.</li>
                <li>Controle de ativos e inventário de hardware e software.</li>
                <li>Monitoramento e manutenção das redes LAN e Wi-Fi, garantindo estabilidade e desempenho.</li>
                <li>Diagnóstico e resolução de problemas de hardware e software, com registro de procedimentos.</li>
                <li>Colaboração com a equipe de TI do cliente para assegurar continuidade das operações.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Experiência 3
    st.markdown(
        """
        <div class="experience-item">
            <h3>Simple Dot Tecnologia da Informação Ltda</h3>
            <p><i class="fa-solid fa-briefcase"></i> Analista de Sistemas ERP</p>
            <p><i class="fa-solid fa-calendar"></i> 10/2022 até 09/2024</p>
            <p><strong>Principais atividades:</strong></p>
            <ul>
                <li>Homologação de documentos de implantação junto aos usuários.</li>
                <li>Implementação e parametrização dos módulos do sistema (retaguarda, PDV, faturamento, pedidos e compras).</li>
                <li>Treinamentos remotos e presenciais para garantir autonomia dos clientes.</li>
                <li>Suporte durante a implantação e fase inicial de uso.</li>
                <li>Acompanhamento de cronograma e alinhamento de demandas entre cliente e equipe interna.</li>
                <li>Liderança em projetos de migração com arquivos CSV e customização de sistemas.</li>
                <li>Configuração de SAT, certificados digitais e formas de pagamento no PDV para conformidade fiscal.</li>
                <li>Capacitação de usuários via Google Meet, Jitsi Meet e AnyDesk, com documentação de processos.</li>
                <li>Testes de sistemas, geração de relatórios de desempenho e suporte técnico pós-implantação.</li>
                <li>Otimização de processos, reduzindo em 30% o tempo de resposta a solicitações de clientes.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        ---
        ### 🚀 Principais Competências
        - Automação de processos em Python e Power Automate
        - Desenvolvimento de aplicações web com Streamlit e Flask, web scraping e integração de APIs
        - Criação de dashboards interativos em Power BI e Python (Plotly, Dash)
        - Criação de fluxos automatizados com Power Automate
        - Suporte técnico e infraestrutura de TI
        - Implementação e treinamento em sistemas ERP/CRM
        """,
        unsafe_allow_html=True,
    )
