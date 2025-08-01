import streamlit as st, requests

st.header('Pokemon Images')
mypokemon=['charizard','pikachu','eevee','snorlax','garchomp','lucario']
pokemon=st.selectbox('Select a Pokemon', mypokemon)
if pokemon:
  r=requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
  for img in r['sprites'].values():
    if img is not None:
      if str(img)[-4:]=='.png':
        st.image(img)
