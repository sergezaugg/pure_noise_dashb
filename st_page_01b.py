#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
from streamlit import session_state as ss
from uele import select_distr_param, select_stored_scenario, prepare_results, make_plot, display_stored_distributions
from utils import update_ss

display_stored_distributions(num_cols = 4, dict_of_distr_params = ss['stored_distr_parameters'])

    

   


       
      
               
       





