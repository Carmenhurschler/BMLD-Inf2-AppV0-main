import streamlit as st
import pandas as pd

st.title("ph-Wert Rechner")
st.write("Hier kannst du per Eingabe von Masse und Molare Masse die Stoffmenge berechnen.")
if st.button("Hier gehts zum Rechner"):
    st.switch_page("pages/1_Rechner.py")  # Überprüfen Sie, ob der Pfad korrekt ist

# WICHTIG: Eure Emails müssen in der App erscheinen!

# Streamlit über den Text unten direkt in die App - cool!
st.markdown("""
Diese App wurde von folgenden Personen entwickelt:
•⁠ Carmen Hurschler (hurscca1@students.zhaw.ch)
""")
