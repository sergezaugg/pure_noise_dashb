#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
import plotly.express as px
from streamlit import session_state as ss
from uele import select_distr_param
from utils import update_ss, plot_scenarios




select_distr_param()


_ = st.selectbox('Select', options = ss['di_li'].keys(), key = "wid02", on_change = update_ss, args=["wid02", "par02"])

fig00 = plot_scenarios(scenarios_di = ss['di_li'][ss["upar"]["par02"]], width = 450, height = 450)

st.plotly_chart(fig00, use_container_width=False, key='k_fig02')










with st.container(height=700, border=True):
    st.text("Session state's internal values") 
    for k in st.session_state:
        st.write(k, st.session_state[k])

