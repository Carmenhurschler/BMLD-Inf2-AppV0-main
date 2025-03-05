import streamlit as st

st.title("Unterseite A")

st.write("Diese Seite ist eine Unterseite der Startseite.")

import streamlit as st


import streamlit as st

# Startseite mit Titel, Beschreibung und Autoren
def startseite():
    st.title("pH-Wert Rechner")
    st.write("""
        Willkommen beim pH-Wert Rechner! 
        Dieser Rechner hilft dir, den pH-Wert einer Lösung basierend auf der Konzentration der Wasserstoffionen (H⁺) zu berechnen.
        
        Der pH-Wert ist ein Mass für den Säuregehalt einer Lösung. 
        Je niedriger der pH-Wert, desto saurer ist die Lösung. Je höher der pH-Wert, desto basischer ist sie.
        
        ### Mitwirkende:
        - Carmen Hurschler (hurscca1@students.zhaw.ch)
        
    """)

# Hauptfunktion zum Starten der App
def main():
    seite = st.sidebar.selectbox("Wähle eine Seite", ["Startseite", "pH-Wert Rechner"])
    
    if seite == "Startseite":
        startseite()
    elif seite == "pH-Wert Rechner":
        from pages import ph_Wert_Rechner  # Aufruf der Unterseite mit Rechner

if __name__ == "__main__":
    main()

import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Funktion zur Berechnung des pH-Werts
def berechne_ph():
    st.title("pH-Wert Rechner")

    # Eingabefeld für Konzentration der Wasserstoffionen (H+)
    h_plus_konzentration = st.number_input("Gib die Konzentration der Wasserstoffionen [H+] in mol/L ein:", min_value=0.0, step=0.0001)

    if h_plus_konzentration > 0:
        # Berechnung des pH-Werts
        ph_wert = -math.log10(h_plus_konzentration)
        
        # Ausgabe des berechneten pH-Werts
        st.write(f"Der berechnete pH-Wert ist: {ph_wert:.2f}")

        # pH-Kategorisierung
        if ph_wert < 7:
            st.write("Die Lösung ist sauer.")
            farbe = 'red'  # Farbe für sauer
        elif ph_wert == 7:
            st.write("Die Lösung ist neutral.")
            farbe = 'yellow'  # Farbe für neutral
        else:
            st.write("Die Lösung ist basisch.")
            farbe = 'blue'  # Farbe für basisch
        
        # Zeige den pH-Wert als farbigen Balken
        zeige_ph_farb_balken(farbe, ph_wert)

    else:
        st.write("Bitte gib eine gültige Konzentration der Wasserstoffionen ein.")

# Funktion zur Darstellung des pH-Werts als farbigen Balken
def zeige_ph_farb_balken(farbe, ph_wert):
    # Erstellen eines farbigen Balkens
    fig, ax = plt.subplots(figsize=(6, 1))  # Balken in horizontaler Form
    ax.barh(0, width=ph_wert, height=1, color=farbe, edgecolor='black')  # Balken mit gewählter Farbe

    # Balken-Beschriftung
    ax.text(ph_wert / 2, 0, f"pH-Wert: {ph_wert:.2f}", color="white", ha='center', va='center', fontsize=12)

    # Entfernen der Achsen und Ticks
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 1)
    ax.set_yticks([])

    # Diagramm-Titel und Legende
    ax.set_title("pH-Wert Visualisierung", fontsize=14)
    
    # Legende hinzufügen
    handles = [
        plt.Line2D([0], [0], marker='s', color='w', label='Sauer (pH < 7)', markerfacecolor='red', markersize=10),
        plt.Line2D([0], [0], marker='s', color='w', label='Neutral (pH = 7)', markerfacecolor='yellow', markersize=10),
        plt.Line2D([0], [0], marker='s', color='w', label='Basisch (pH > 7)', markerfacecolor='blue', markersize=10),
    ]
    ax.legend(handles=handles, loc='lower center', bbox_to_anchor=(0.5, -0.2), shadow=True)

    # Diagramm anzeigen
    st.pyplot(fig)

# Aufruf der Funktion zur Berechnung
if __name__ == "__main__":
    berechne_ph()