#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
from streamlit import session_state as ss
from uele import display_stored_distributions

display_stored_distributions(num_cols = 4, dict_of_distr_params = ss['stored_distr_parameters'])

    

   


       
      
               
       





