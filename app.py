import openpyxl
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_excel(r'censo_1872.xlsx', engine='openpyxl')
df = df.drop_duplicates()

df = df.dropna()
soma = df.sum()


homens_livres = soma.loc["homens_livres"]

homens_livres = (soma.loc["homens_livres"])
homens_escravizados = (soma.loc["homens_escravizados"])
mulheres_livres = (soma.loc["mulheres_livres"])
mulheres_escravizadas = (soma.loc["mulheres_escravizadas"])

percentual_hl = (homens_livres / (homens_livres + homens_escravizados) * 100)
percentual_he = (homens_escravizados / (homens_livres + homens_escravizados)*100)
percentual_ml = (mulheres_livres / (mulheres_livres + mulheres_escravizadas)*100)
percentual_me = (mulheres_escravizadas / (mulheres_livres + mulheres_escravizadas)*100)



st.title("escravizados censo de 1872")
st.header("relação entre homens e mulheres escravizados e soltos")


visualizacao = st.sidebar.selectbox(
    "Escolha uma opção de visualização 📊",
    ["Tabela", "Gráfico"]
)
total_livres = soma.loc['total_livres']

if visualizacao == "Tabela":
    final = {
    "total livres" : total_livres,
    "porcentagem homens livres" : percentual_hl,
    "porcentagem homens escravizados" : percentual_he,
    "mulheres livres" : percentual_ml,
    "mulheres escravizadas" : mulheres_escravizadas
    }
    st.dataframe(final)

else:
    col1, col2 = st.columns(2)

    with col1:
        dados = {
            "homensLivres" : percentual_hl,
            "homensEscravizados" : percentual_he,
            "totalLivres" : total_livres
        }
        df = pd.DataFrame(dados, index=[0,1])

        fig =  fig = px.pie(
            names=["Homens livres","Homens escravizados"],
            values=[homens_livres,homens_escravizados],
            color="totalLivres",
            data_frame=df
            
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.caption(
            "Homens livres x homens escravizados"
        )
    with col2:
        
        dados = {
            "mulheresLivres" : percentual_ml,
            "mulheresEscravizadas" : percentual_me,
            "totalLivres" : total_livres
        }

        df = pd.DataFrame(dados, index=[0,1])
        fig = px.pie(
            names=["mulheres livres","mulheresescravizadas"],
            values=[mulheres_livres,mulheres_escravizadas],
            color="totalLivres",
            data_frame=df
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.caption(
            "mulheres livres x mulheres escravizadas"
        )



