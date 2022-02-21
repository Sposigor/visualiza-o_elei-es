""" Vamos criar algumas visualizações sobre o periodo eleitoral do pais """


import pandas as pd
import streamlit as st
from opcao_grafico import visualiza_grafico
from opcao_tabela import visualizar_tabela

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

if tipo_visualização == "Gráfico":
    visualiza_grafico()
else:
    visualizar_tabela()
