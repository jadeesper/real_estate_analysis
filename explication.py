import streamlit as st

st.sidebar.markdown("Explication et origine des données")

st.markdown("Explication et origine des données")
temp_var = st.number_input('enter celcius')
st.write(f'fahrenheit is: {temp_var*9/5+32}F')


