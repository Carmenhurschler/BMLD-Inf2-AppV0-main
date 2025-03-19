# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======
 
# ------------------------------------------------------------
 
import streamlit as st

st.title('pH-Wert Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine pH-Wert Daten vorhanden. Berechnen Sie Ihren pH-Wert auf der Startseite.')
    st.stop()

# pH over time
st.line_chart(data=data_df.set_index('timestamp')['pH_wert'], 
                use_container_width=True)
st.caption('pH-Wert über Zeit')




