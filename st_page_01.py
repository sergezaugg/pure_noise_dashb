#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
import plotly.express as px
from streamlit import session_state as ss
from uele import select_distr_param, select_stored_scenario
from utils import update_ss, plot_scenarios , evaluate_scenarios_rfo




select_distr_param()

select_stored_scenario()



if len(ss["upar"]["par02"]) > 0:

    with st.form("f03", border=False, clear_on_submit=True, enter_to_submit=False):

        nb_noisy_features = [0, 1, 5, 10, 50, 100]
        nb_trees = 10

        submitted3 = st.form_submit_button("Start simulation", type="primary", use_container_width = True)   
        if submitted3:
            resu01 = evaluate_scenarios_rfo(sce = ss['di_li'][ss["upar"]["par02"]], 
                nb_noisy_features = nb_noisy_features,  
                ntrees = nb_trees, 
                rfo_max_features = 1, 
                seed = 888)
            ss['resu'].append(resu01)
            # st.dataframe(resu01['df_result'])







with st.container(height=700, border=True):
    st.text("Session state's internal values") 
    for k in st.session_state:
        st.write(k, st.session_state[k])



