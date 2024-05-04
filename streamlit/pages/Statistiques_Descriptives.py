import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objs as go


st.sidebar.markdown("Analyse des biens")



data = pd.read_csv('Clean_data.csv')

data['espace_suppl'] = data['caves'] + data['sous_sol']
data['espace_ext'] = data['terrasses'] + data['balcons']
data['parking'] = data['place_parking'] + data['garages']


#1ere figure
counts = data['type'].value_counts()
fig1 = px.bar(counts, x=counts.index, y=counts.values, text=counts.values, color='type')
fig1.update_layout(title='Comptage de chaque type de logement')

#2e figure
fig2 = px.scatter(data, x='surface', y='prix')
fig2.update_layout(yaxis2=dict(title="Prix (en milliers d'euros)", 
                              titlefont=dict(color='red'), 
                              tickfont=dict(color='red'), 
                              overlaying='y', 
                              side='right'))

fig2.update_layout(
    title='Evolution du prix en fonction de la surface',
    xaxis_title='Surface (mètres carrés)',
    yaxis_title="Prix (milliers d'euros)"
)

#3e figure
data2 = data[data['annee_constr'] > 1800]
fig3 = px.scatter(data2, x='annee_constr', y='prix', trendline='ols')
fig3.update_layout(title="Evolution des prix en fonction de l'année de contruction des biens")

#4e figure
grouped = data.groupby('piscine').mean()
fig4 = px.bar(grouped, x=grouped.index, y='prix', color='prix')
fig4.update_layout(title="Prix moyen en fonction de la présence ou non de piscine")



#5e figure
terrain_count = data['terrain'].value_counts()
ascenseur_count = data['ascenseur'].value_counts()
cuisine_count = data['cuisine_amenagee'].value_counts()
cave_count = data['espace_suppl'].value_counts()
ext_count = data['espace_ext'].value_counts()
parking = data['parking'].value_counts()
fig5 = sp.make_subplots(rows=2, cols=3)
trace1 = go.Bar(x=['Oui', 'Non'], y=terrain_count, name='Terrain')
trace2 = go.Bar(x=['Oui', 'Non'], y=ascenseur_count, name='Ascenseur')
trace3 = go.Bar(x=['Oui', 'Non'], y=cuisine_count, name='Cuisine Aménagée')
trace4 = go.Bar(x=['Oui', 'Non'], y=cave_count, name='Cave ou sous-sol')
trace5 = go.Bar(x=['Oui', 'Non'], y=ext_count, name='Terrasse ou Balcon')
trace6 = go.Bar(x=['Oui', 'Non'], y=parking, name='Parking ou garage')
fig5.add_trace(trace1, row=1, col=1)
fig5.add_trace(trace2, row=1, col=2)
fig5.add_trace(trace3, row=1, col=3)
fig5.add_trace(trace4, row=2, col=1)
fig5.add_trace(trace5, row=2, col=2)
fig5.add_trace(trace6, row=2, col=3)
fig5.update_layout(
    title='Présence ou non de caractéristiques dans les logements'
)



# Streamlit layout
st.title('Visualisation des données')

st.plotly_chart(fig1)
st.write("Les données sont relativement bien réparties entre appartements et maisons, avec la présence d'une observation 'Loft' ")

st.subheader("Il est intéressant de se pencher sur les prix des biens:")

st.plotly_chart(fig2)
st.write("""On observe une relation relativement croissante entre la surface du bien et son prix.
On voit que la plupart des valeurs sont concentrées entre 0 et 100 mètres carrés, et sur des prix allant jusqu'à 500 000. """)

st.plotly_chart(fig3)
st.write("On voit, à travers ce graphique, que l'année de construction du bien n'influe pas beaucoup sur son prix.")

st.plotly_chart(fig4)
st.write("Les biens qui comportent une piscine sont en moyenne beaucoup plus chers que ceux qui n'en ont pas")

st.subheader("On peut aussi observer les caractéristiques par bien:")
st.plotly_chart(fig5)
st.write("Certaines caractéristiques sont très présentes dans les logements du site, comme la présence d'ascencseur ou de place de parking. La caractéristique la plus nuancée est la présence de cave ou de sous-sol.")



