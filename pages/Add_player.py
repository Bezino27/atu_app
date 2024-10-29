import streamlit as st
from functions import add_players

st.header('Add Player')

col1, col2, col3 = st.columns(3)
with col1:
    meno=st.text_input("Zadajte meno a priezvisko hráča")

with col2:
    rok=st.text_input("Zadajte rok narodenia")

with col3:
    mail=st.text_input("Zadajte email")

if st.button("Pridať hráča"):
    if meno and rok and mail:
        add_players(meno,int(rok),mail)
        st.write(f"Hráč {meno}, narodený v roku {rok}, s emailom {mail} bol úspešne pridaný!")
    else:
        st.write("Vyplňte prosím všetky polia.")