#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from streamlit import session_state as ss
from uele import select_distr_param, select_stored_scenario, prepare_results, make_plot


select_distr_param()

select_stored_scenario()

if len(ss['resu']) > 0:

    ss['dfresu'] = prepare_results(li = ss['resu'])

    make_plot(df = ss['dfresu'], width = ss["upar"]["par10"], height=ss["upar"]["par11"])






   







