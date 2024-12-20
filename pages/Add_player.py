import streamlit as st
from PIL.ImImagePlugin import number

from functions import add_players

st.header('Add Player')

col1, col2, col3, col4 = st.columns(4)
with col1:
    cislo=st.text_input('Zadajte číslo')
with col2:
    meno=st.text_input("Zadajte meno a priezvisko hráča")

with col3:
    rok=st.text_input("Zadajte rok narodenia")

with col4:
    mail=st.text_input("Zadajte email")

if st.button("Pridať hráča"):
    if cislo.isnumeric() and meno and rok.isnumeric() and mail:
        add=add_players(cislo,meno,int(rok),mail)
        if add == False:
            st.write("Zadali ste nesprávne údaje")
        elif add == 1:
            st.write("Tento hráč sa už nachádza v našej databáze")
        else:
            st.write(f"Hráč {meno}, narodený v roku {rok}, s emailom {mail} bol úspešne pridaný!")
    else:
        st.write("Vyplňte prosím všetky polia.")