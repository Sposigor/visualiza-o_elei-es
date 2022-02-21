""" Visualização dos dados """

import pandas as pd
import plotly.express as px
import streamlit as st
from estados_municipios import retornaEstado, retornaMunicipios

def visualiza_grafico():

    nivel = st.sidebar.selectbox("Nível de Governo", ["Nacional", "Estadual", "Municipal"])

    if nivel == "Estadual":
        cargo_politico = st.sidebar.selectbox("Selecione o cargo", ["Deputado Federal", "Deputado Estadual", "Governador", "Senador"], index=2).upper()
        estado = st.sidebar.selectbox("Selecione o estado", retornaEstado(), index=25)
        df = pd.read_csv(r"dados/federal_ajustado.csv", sep=",")
        ano = st.sidebar.slider("Selecione o ano", 1998, 2018, step=4)
        grafico = df.query(f"ANO_ELEICAO == {ano} and UF == '{estado}' and DESCRICAO_CARGO == '{cargo_politico}'")
        colormap = {'PRIMEIRO TURNO':"#FFFF00", 'SEGUNDO TURNO':"#000080"}

        fig = px.bar(grafico, y='QTDE_VOTOS', x='NOME_CANDIDATO', text_auto='.2s', color="NUM_TURNO", color_discrete_map=colormap,
                title=f"Eleições no Estado de {estado} para {cargo_politico.capitalize()} no ano de {ano}", opacity=0.8, orientation="v", barmode="relative", 
                height=600, template="simple_white", labels={'NOME_CANDIDATO':'Nome do Candidato', 'QTDE_VOTOS':'Quantidade de Votos', 'NUM_TURNO':'Turno'})
    
        st.plotly_chart(fig, use_container_width=True)

    elif nivel == "Municipal":
        cargo_politico = st.sidebar.selectbox("Cargo", ["Prefeito"]).upper()
        estado = st.sidebar.selectbox("Selecione o estado", retornaEstado(), index=25)
        municipio = st.sidebar.selectbox("Selecione o município", retornaMunicipios(estado), index=562).title()
        df = pd.read_csv(r"dados/prefeito_ajustado.csv", sep=",")
        ano = st.sidebar.slider("Selecione o ano", 2000, 2016, step=4)
        grafico = df.query(f"ANO_ELEICAO == {ano} and UF == '{estado}' and NOME_MUNICIPIO == '{municipio}'")
        colormap = {'PRIMEIRO TURNO':"#FFFF00", 'SEGUNDO TURNO':"#000080"}

        fig = px.bar(grafico, y='QTDE_VOTOS', x='NOME_CANDIDATO', text_auto='.2s', color="NUM_TURNO", color_discrete_map=colormap,
                title=f"Eleições no municipio de {municipio.capitalize()} no estado de {estado} para {cargo_politico.capitalize()} no ano de {ano}", opacity=0.8, orientation="v", barmode="relative", 
                height=600, template="simple_white", labels={'NOME_CANDIDATO':'Nome do Candidato', 'QTDE_VOTOS':'Quantidade de Votos', 'NUM_TURNO':'Turno'})
    
        st.plotly_chart(fig, use_container_width=True)

    else:
        df = pd.read_csv(r"dados/presidente_ajustado.csv", sep=",")
        cargo_politico = st.sidebar.selectbox("Cargo", ["Presidente"])
        ano = st.sidebar.slider("Selecione o ano", 1998, 2018, step=4)
        grafico = df.query(f"ANO_ELEICAO == {ano}")
        colormap = {'PRIMEIRO TURNO':"#FFFF00", 'SEGUNDO TURNO':"#000080"}

        fig = px.bar(grafico, y='QTDE_VOTOS', x='NOME_CANDIDATO', text_auto='.2s', color="NUM_TURNO", color_discrete_map=colormap,
                title=f"Eleições no Brasil para {cargo_politico.capitalize()} no ano de {ano}", opacity=0.8, orientation="v", barmode="relative", 
                height=600, template="simple_white", labels={'NOME_CANDIDATO':'Nome do Candidato', 'QTDE_VOTOS':'Quantidade de Votos', 'NUM_TURNO':'Turno'})
        st.plotly_chart(fig, use_container_width=True)
