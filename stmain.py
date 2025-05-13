#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# Run locally : streamlit run stmain.py
#--------------------

import streamlit as st
from streamlit import session_state as ss
import numpy as np

# (1) ---------------------
# set initial session state

# set initial scenario parameters 
init_distr =  {
    'n1' : 2000, 'mu1' : [0.0, 0.0] , 'std1' : [1.0, 1.0], 'corr1' : 0.0,
    'n2' : 2000, 'mu2' : [0.0, 0.0] , 'std2' : [1.0, 1.0], 'corr2' : 0.0,
    }
if 'distr' not in ss:
    ss['distr'] = init_distr

# dict to track distribution that were stored by user 
if 'stored_distr_parameters' not in ss:
    ss['stored_distr_parameters'] = {}
    ss['stored_distr_parameters']['Please create a scenario'] = "initial" # {}

# keep track of user-provided params
if 'upar' not in ss:
    ss["upar"] = {
        "par02" : "initial",
        "par03" : 2**np.arange(0,10,1), # [1,10,100,1000], 
        "par04" : 1, 
        "par05" : 10, 
        "par10" : 1000, 
        "par11" : 500, 
        "col_a" : '#FF00FF',
        "col_b" : '#6AFF00',
        "col_seq" : ['#ff0000', '#ffff66', '#33ff00', '#00ffff', '#ffbb00', '#ff00ff', '#0077ff',]
        }



# keep track of intermediate computation results
if 'resu' not in ss:
    ss['resu'] = []

if 'dfresu' not in ss:
    ss['dfresu'] = []

# keep track of counters 
if 'run_nb' not in ss:
    ss['run_nb'] = 0

if 'num_index_sce' not in ss:
    ss['num_index_sce'] = 0

if 'sce_counter' not in ss:
    ss['sce_counter'] = 0


# -------------------
# (2) main navigation

st.set_page_config(layout="wide")
 
pages = [
    st.Page("st_page_01.py",  title="Simulate"),
    st.Page("st_page_01b.py", title="Stored scenarios"),
    st.Page("st_page_03.py",  title="Settings"),
    st.Page("st_page_00.py",  title="Summary"),
    st.Page("st_page_02.py",  title="Example"),
    ]

pg = st.navigation(pages)

pg.run()

with st.sidebar:
    st.text("v0.6.0 - under devel")

    st.markdown(''':blue[QUICK GUIDE]''')
    st.text("(1) Define and store one or several distributional scenarios.")
    st.text("(2) Define nb of pure-noise-features and Random Forest parameters and run simulations.")
    st.text("(3) Check the plotted results to compare scenarios and Random Forest parameters.")

    st.title(""); st.title(""); st.title(""); 
    st.title(""); st.title("")
    st.markdown(''':gray[RELATED TOPICS]''')
    st.page_link("https://ml-performance-metrics.streamlit.app/", label=":gray[ml-performance-metrics]")
    st.page_link("https://featureimportance.streamlit.app/", label=":gray[feature-importance:red]")
