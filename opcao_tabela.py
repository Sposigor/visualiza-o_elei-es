""" Tabela dos dados """

import pandas as pd
import streamlit as st



def visualizar_tabela():
    nivel = st.sidebar.selectbox("Nível de Governo", ["Nacional", "Estadual", "Municipal"])

    if nivel == "Estadual":
        df = pd.read_csv(r"dados/federal_ajustado.csv", sep=",")
        st.dataframe(df.head(10))
        csv = convert_df(df)
        st.download_button(
            label="Download em CSV",
            data=csv,
            file_name='dados_estaduais.csv',
            mime='text/csv',
        )

    elif nivel == "Municipal":
        df1 = pd.read_csv(r"dados/prefeito_ajustado.csv", sep=",")
        st.dataframe(df1.head(25))
        csv1 = convert_df(df1)
        st.download_button(
            label="Download em CSV",
            data=csv1,
            file_name='dados_municipais.csv',
            mime='text/csv',
        )

    else:
        df2 = pd.read_csv(r"dados/presidente_ajustado.csv", sep=",")
        st.dataframe(df2.head(25))
        csv2 = convert_df(df2)
        st.download_button(
            label="Download em CSV",
            data=csv2,
            file_name='dados_presidenciais.csv',
            mime='text/csv',
        )

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')