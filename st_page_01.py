#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from streamlit import session_state as ss
from uele import select_distr_param, select_stored_scenario, prepare_results, make_plot, plot_scenarios, display_plots_on_grid
from utils import update_ss

select_distr_param()

# display plots in a regular grid 
if not ss["upar"]["par02"] == 'initial':
    display_plots_on_grid(num_cols = 4, dict_of_distr_params = ss['stored_distr_parameters'])

select_stored_scenario()


if len(ss['resu']) > 0:

    ss['dfresu'] = prepare_results(li = ss['resu'])
    
    with st.expander("(3) Check simulation results (click to expand/collapse)", expanded=True):
        CA, CB, = st.columns([0.80, 0.10])
        with CA:
            make_plot(df = ss['dfresu'], width = ss["upar"]["par10"], height=ss["upar"]["par11"])
        with CB:
            st.text("Line-plot size")
            _ = st.slider("Width",  min_value=100, max_value=1500, value=ss["upar"]["par10"], step=100, key="wid10", on_change=update_ss, args=["wid10", "par10"])
            _ = st.slider("Height", min_value=100, max_value=1500, value=ss["upar"]["par11"], step=100, key="wid11", on_change=update_ss, args=["wid11", "par11"])


    

   


       
      
               
       





