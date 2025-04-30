#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st


st.text("debuggin info")



with st.container(height=700, border=True):
    st.text("Session state's internal values") 
    for k in st.session_state:
        st.write(k, st.session_state[k])



