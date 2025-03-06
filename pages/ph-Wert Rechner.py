import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Titel der App
st.title("pH-Wert Rechner")
st.header("Berechnung des pH-Werts")

# Home Button für Navigation (Beachte: Der Name der Seite sollte ohne `.py` sein)
if st.button("Home"):
    st.switch_page("Start.py")

    # Bonus-Tipp: Textfeld, um den pH-Wert zu erklären
    st.write("""
        **Erklärung der Kategorien:**
        - **Sauer:** Ein pH-Wert unter 7 bedeutet, dass die Lösung sauer ist (z.B. Zitronensaft, Essig).
        - **Neutral:** Ein pH-Wert von 7 bedeutet, dass die Lösung weder sauer noch basisch ist (z.B. reines Wasser).
        - **Basisch:** Ein pH-Wert über 7 bedeutet, dass die Lösung basisch ist (z.B. Seifenlösung, Natronlauge).
    """)


# Option zur Eingabe des pH-Werts oder zur Berechnung mit [H+]
berechnen_mit = st.radio("Wie möchtest du den pH-Wert berechnen?", ('Direkt eingeben', 'Berechnen mit [H+]'))

if berechnen_mit == 'Direkt eingeben':
    pH_wert = st.number_input("Gib den pH-Wert ein:", min_value=0.0, max_value=14.0, step=0.1)
else:
    # Eingabe der Konzentration von Wasserstoffionen [H+]
    h_plus_konzentration = st.number_input("Gib die Konzentration der Wasserstoffionen [H+] in mol/L ein:", min_value=0.0, step=0.0001)
    if h_plus_konzentration > 0:
        pH_wert = -np.log10(h_plus_konzentration)  # Berechnung des pH-Werts
    else:
        pH_wert = None  # Falls die Konzentration 0 ist, ist der pH-Wert nicht definiert

# Berechnung der Kategorie
if pH_wert is not None:
    if pH_wert < 7:
        kategorie = "Sauer"
        farbe = 'lightcoral'
    elif pH_wert == 7:
        kategorie = "Neutral"
        farbe = 'lightblue'
    else:
        kategorie = "Basisch"
        farbe = 'lightgreen'

    # Anzeige der Kategorie
    st.write(f"Der pH-Wert von {pH_wert:.2f} ist {kategorie}.")
    
    # Erstellen eines Balkendiagramms mit Pastellfarben
    labels = ['Sauer', 'Neutral', 'Basisch']
    values = [max(0, 7 - pH_wert), 0 if pH_wert != 7 else 1, max(0, pH_wert - 7)]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['lightcoral', 'lightblue', 'lightgreen'])

    # Diagramm anzeigen
    ax.set_ylabel('Wert')
    ax.set_title(f'Kategorisierung des pH-Werts: {kategorie}')
    st.pyplot(fig)

    # Bonus-Tipp: Textfeld, um den pH-Wert zu erklären
    st.write("""
        **Erklärung der Kategorien:**
        - **Sauer:** Ein pH-Wert unter 7 bedeutet, dass die Lösung sauer ist (z.B. Zitronensaft, Essig).
        - **Neutral:** Ein pH-Wert von 7 bedeutet, dass die Lösung weder sauer noch basisch ist (z.B. reines Wasser).
        - **Basisch:** Ein pH-Wert über 7 bedeutet, dass die Lösung basisch ist (z.B. Seifenlösung, Natronlauge).
    """)
else:
    st.write("Die Konzentration der Wasserstoffionen [H+] muss größer als 0 sein, um den pH-Wert zu berechnen.")
