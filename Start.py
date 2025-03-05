import streamlit as st
import pandas as pd

st.title("ph-Wert Rechner")
st.write("Willkommen beim pH-Wert Rechner! Diese App hilft dir, den pH-Wert einer Lösung zu bestimmen und herauszufinden, ob sie sauer, neutral oder basisch ist – ganz einfach und schnell!")

# Button zum Wechseln zur Seite "ph-Wert Rechner"
if st.button("Rechner"):
    st.switch_page("pages/ph-Wert Rechner.py")

# WICHTIG: Eure Emails müssen in der App erscheinen!

# Streamlit über den Text unten direkt in die App - cool!
st.markdown("""
Diese App wurde von Carmen Hurschler (hurscca1@students.zhaw.ch) im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW entwickelt.
            
""")
