import streamlit as st
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration de la page (DOIT être la première commande Streamlit)
st.set_page_config(page_title='Real Time Science Dashboard',
                   page_icon='😇✅🤗', layout='wide')

# Chargement des données
df = pd.read_csv('bank.csv')

st.title("Real Time / Live Data Analysis")

# Filtre sur le type de job
# Correction : st.selectbox et df.unique
job_filter = st.selectbox("Select a job", df["job"].unique())

# Application du filtre
df_selection = df[df["job"] == job_filter] 

# CALCUL DES INDICATEURS (KPIs)
avg_age = np.mean(df_selection["age"])
# Correction : 'married' avec deux 'r'
count_married = int(df_selection[df_selection["marital"] == 'married']['marital'].count())
balance = np.mean(df_selection["balance"])

# Création des colonnes pour les KPIs
kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(label='Âge moyen ⏳', value=round(avg_age), delta=round(avg_age))
# Correction : kpi2, delta (au lieu de detta) et fermeture de la parenthèse )
kpi2.metric(label='Mariés 💍', value=count_married, delta=count_married)
kpi3.metric(label='Balance moyenne $', value=f"${round(balance,2)}",
            delta=-round(balance/max(1, count_married))*100)

# GRAPHIQUES
col1, col2 = st.columns(2)

with col1:
    st.markdown('### RÉPARTITION PAR STATUT MATRIMONIAL')
    fig1 = plt.figure() # Correction : fig1 (sans espace)
    sns.barplot(data=df_selection, y='age', x='marital', palette='mako')
    st.pyplot(fig1)

with col2:
    st.markdown('### DISTRIBUTION DES ÂGES')
    fig2 = plt.figure() # Correction : fig2 (sans espace)
    sns.histplot(data=df_selection, x='age', kde=True) # Correction : x='age' pour un histogramme classique
    st.pyplot(fig2)
    
st.markdown('### VUE DÉTAILLÉE DES DONNÉES')
st.dataframe(df_selection)