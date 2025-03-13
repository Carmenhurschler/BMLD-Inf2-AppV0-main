import streamlit as st
import pandas as pd

from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

# === Initialize the login manager ===
from utils.login_manager import LoginManager

login_manager = LoginManager(data_manager) # initialize login manager
login_manager.login_register()  # opens login page

#Start with actual app

st.title("ph-Wert Rechner")
st.info("Willkommen beim pH-Wert Rechner! Diese App hilft dir, den pH-Wert einer Lösung zu bestimmen und herauszufinden, ob sie sauer, neutral oder basisch ist – ganz einfach und schnell!")

# Button zum Wechseln zur Seite "ph-Wert Rechner"
if st.button("Rechner"):
    st.switch_page("pages/ph-Wert Rechner.py")

# WICHTIG: Eure Emails müssen in der App erscheinen!

# Streamlit über den Text unten direkt in die App - cool!
st.markdown("""
Diese App wurde von Carmen Hurschler (hurscca1@students.zhaw.ch) im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW entwickelt.
            
""")
