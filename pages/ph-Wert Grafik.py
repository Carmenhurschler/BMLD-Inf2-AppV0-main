import streamlit as st

st.title('pH-Wert Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine pH-Wert Daten vorhanden. Berechnen Sie Ihren pH-Wert auf der Startseite.')
    st.stop()

# Weight over time
st.line_chart(data=data_df.set_index('timestamp')['H+ in mol/l'], 
                use_container_width=True)
st.caption('pH-Wert über Zeit (mol/l)')

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['ph'],
                use_container_width=True)
st.caption('Größe über Zeit (m)')

# BMI over time
st.line_chart(data=data_df.set_index('timestamp')['pH'],
                use_container_width=True)
st.caption('pH-Wert über Zeit')