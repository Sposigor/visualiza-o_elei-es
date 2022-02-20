""" Vamos criar algumas visualizações sobre o periodo eleitoral do pais """


import pandas as pd
import streamlit as st
from estados_municipios import retornaEstado, retornaMunicipios

# Configurações do streamlit para a pagina web
st.set_page_config(
    page_title="Eleições no Brasil",
    page_icon="🇧🇷",
    layout="wide",
    initial_sidebar_state="expanded"
    )


# Header - da pagina com informações sobre o app
st.title("Eleições no Brasil desde 1998")
with st.expander("Urna eletrônica: o marco democratico brasileiro"):
            st.write(
                """
O pleito de 1998 foi o primeiro pleito eleitoral brasileiro aonde todos os brasileiros aptos a votar, votaram no sistema eleitoral eletrônico.

* **Impactos:** introdução da urna eletrônica produziu um acréscimo de aproximadamente 12 pontos percentuais na proporção de votos válidos, de um pouco mais de 75% nos municípios que utilizavam cédulas em papel para cerca de 90% para as localidades com urnas eletrônicas.
* **Curiosidade:** Em 1996, somente municípios com mais de 40.500 eleitores utilizaram a nova tecnologia. Nos demais casos, os votos foram por meio de cédulas em papel (exceção feita aos estados de Amapá, Roraima, Alagoas e Rio de Janeiro, que adotaram a urna eletrônica em todas as localidades).
* **fonte sobre a urna eletrônica:** https://www.tse.jus.br/eleicoes/urna-eletronica
* **fonte sobre os impactos:** https://www.princeton.edu/~fujiwara/papers/elecvote_site.pdf
""")


# Barra lateral para seleção das opções - variaveis
st.sidebar.title("Selecionar as opções:")

tipo_visualização = st.sidebar.selectbox("Selecione o tipo de visualização", ["Gráfico", "Tabela"])

nivel = st.sidebar.selectbox("Nível de acesso", ["Nacional", "Estadual", "Municipal"])

if nivel == "Estadual":
    estado = st.sidebar.selectbox("Selecione o estado", retornaEstado())
    cargo_politico = st.sidebar.selectbox("Selecione o cargo", ["Deputado Federal", "Deputado Estadual", "Governador", "Senador"])
    
elif nivel == "Municipal":
    estado = st.sidebar.selectbox("Selecione o estado", retornaEstado())
    municipio = st.sidebar.selectbox("Selecione o município", retornaMunicipios(estado))

anos_federal_estadual = (1998, 2002, 2006, 2010, 2014, 2018)
anos_municipais = (2000, 2004, 2008, 2012, 2016)

if nivel in ("Estadual", "Nacional"):
    ano = st.sidebar.slider("Selecione o ano", 1998, 2018, step=4)
else:
    ano = st.sidebar.slider("Selecione o ano", 2000, 2016, step=4)


consultar = st.sidebar.selectbox("Consultar", ["Resultado Eleitoral", "Caracteristicas dos Candidatos"])

if consultar == "Resultado Eleitoral":
    st.sidebar.markdown("""Resultado Eleitoral, é o resultado dos candidatos eleitos e não eleitos e o total de votos.""")
else:
    st.sidebar.markdown("""Informações sobre idade, raça e escolaridade dos candidatos por estado""")
