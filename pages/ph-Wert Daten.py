import streamlit as st

# Titel der App
st.title('pH-Wert Daten')

# Überprüfen, ob pH-Wert Daten vorhanden sind
data_df = st.session_state.get('data_df', None)
if data_df is None or data_df.empty:
    st.info('Keine pH-Wert Daten vorhanden. Berechnen Sie Ihren pH-Wert auf der Startseite.')
    st.stop()

# Sortiere das DataFrame nach dem Zeitstempel
data_df = data_df.sort_values('timestamp', ascending=False)

# Anzeige der Tabelle
st.dataframe(data_df)

# Home Button für Navigation
if st.button("Home"):
    st.switch_page("Start.py")