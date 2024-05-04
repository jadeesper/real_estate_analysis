import streamlit as st
import pandas as pd


st.title('Laforet Helping Tool')
st.subheader("Un outil pour vous aider à mieux visualiser les caractéristiques des biens sur le site Laforet.com")
st.write("Jade Esper & Esteban Mauboussin - M2 MoSEF")

data = pd.read_csv('Clean_data.csv')

#Streamlit layout
st.markdown(
    """Dans le but d'avoir une meilleure visualisation des logements sur le site LaForet, 
     nous avons décidé de créer une base de données par Webscraping du site.\n On essaie, pour chaque annonce, de récuperer les élments
     qui caractérisent les logements (On se concentre donc uniquement sur les maisons et les appartments).
      Voici l'affichage typique d'une annonce sur la page générale de recherche : """)


st.image('annonce.png')

st.markdown(
    """Certaines caractéristiques sont présentes directement sur l'annonce, mais la plupart sont en fait
    cachées sur la page complète de l'annonce: """)


st.image('caracteristiques.png')

st.markdown(
    """Pour chacune des annonces, on extrait les informations de sa page complète. 
    Après nettoyage des données et ajout de features en partant de notre scraping, voici à quoi ressemble notre base de données :""")
st.write(data.head())
st.write("La forme de la base de données totale est:", data.shape)


