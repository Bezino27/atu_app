import streamlit as st
import functions as fn
from functions import view_by_category, get_players_by_year
st.cache_data.clear()
year=2024
choices=["Mladšia prípravka","Staršia prípravka","Mladší žiaci","Starší žiaci","Dorastenci","Juniori","Muži"]

st.header("Zoznam hráčov")
choice=st.selectbox("Vyber kategóriu",choices)
zoznam=fn.view_by_category(choice,year)
for players in zoznam:
    st.write(players)

#fn.add_players("Tomáš Bezeg", 2003, "tomikbez@gmail.com")
#fn.view_by_category("dorastenci",2024)
#fn.delete_player("Tomáš Bezeg",2003)
#fn.get_players_by_year(2003)
#fn.edit_player("Martin Guľaš", 2009)
#index=fn.get_player_index("Oliver Olekšák", 2009, "denisa.oleksakova@gmail.com")
#print(index)