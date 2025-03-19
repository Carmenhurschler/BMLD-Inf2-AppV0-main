import streamlit as st

# Titel der App
st.title('pH-Wert Verlauf')

# Überprüfen, ob pH-Wert Daten vorhanden sind
data_df = st.session_state.get('data_df', None)
if data_df is None or data_df.empty:
    st.info('Keine pH-Wert Daten vorhanden. Berechnen Sie Ihren pH-Wert auf der Startseite.')
    st.stop()

# pH-Wert Verlauf über Zeit anzeigen
st.line_chart(data=data_df.set_index('timestamp')['pH_wert'], use_container_width=True)
st.caption('pH-Wert über Zeit')

# Kategorisierung (Sauer, Neutral, Basisch) über Zeit anzeigen
# Hier nehmen wir die Kategorie basierend auf dem pH-Wert (z.B. 'Sauer', 'Neutral', 'Basisch')
data_df['Kategorie'] = data_df['pH_wert'].apply(lambda x: 'Sauer' if x < 7 else ('Neutral' if x == 7 else 'Basisch'))

# Kategorisierung über Zeit anzeigen
st.line_chart(data=data_df.set_index('timestamp')['Kategorie'].map({
    'Sauer': 0,
    'Neutral': 1,
    'Basisch': 2
}), use_container_width=True)
st.caption('Kategorisierung des pH-Werts (0= Sauer, 1= Neutral, 2= Basisch)')

# Home Button für Navigation
if st.button("Home"):
    st.switch_page("Start.py")