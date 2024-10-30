import streamlit as st
from PIL.ImImagePlugin import number

from functions import delete_player

st.header('Delete Player')

col1, col2 = st.columns(2)
with col1:
    meno=st.text_input("Zadajte meno a priezvisko hráča")

with col2:
    rok=st.text_input("Zadajte rok narodenia")


if st.button("Vymaž hráča"):
    if meno and rok.isnumeric():
        delete=delete_player(meno,int(rok))
        if delete == True:
            st.write(f"Hráč {meno}, narodený v roku {rok} bol úspešne vymazaný!")
        else:
            st.write("Zadali ste nesprávane údaje")

    else:
        st.write("Vyplňte prosím všetky polia.")