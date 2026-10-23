#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# Run locally : streamlit run stmain.py
#--------------------

import streamlit as st
from streamlit import session_state as ss
import numpy as np
from resources.styles import apply_global_styles

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="pure-noise-features", page_icon='pics/z_logo_violet.png')
apply_global_styles() # apply custom CSS styles 

# add main title in top bar via CSS 
st.markdown("""
<style>
    .app-title {
        position: fixed;
        top: +13px;  /* decrease to move up */
        font-size: 27px;
        font-weight: 600;
        color: #a064ff;
        z-index: 999999;
        pointer-events: none;
    }
</style>
<div class="app-title">Impact of pure-noise-features on predictive performance of ML models</div>
""", unsafe_allow_html=True)

# (1) ---------------------
# set initial session state

# set initial scenario parameters 
init_distr =  {
    'n1' : 2000, 'mu1' : [0.0, 0.0] , 'std1' : [1.0, 1.0], 'corr1' : 0.9,
    'n2' : 2000, 'mu2' : [0.0, 0.0] , 'std2' : [1.0, 1.0], 'corr2' : -0.9,
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
        "par03" : 2**np.arange(0,10,1),  
        "par04" : 1, 
        "par05" : 10, 
        "par10" : 1000, 
        "par11" : 500, 
        "col_a" : '#FF00FF',
        "col_b" : '#0077ff',
        "col_seq" : ['#ff0000', '#ffff66', '#33ff00', '#00ffff', '#ffbb00', '#ff00ff', '#0077ff',],
        "test_size_prop" : 0.5,
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

pages = [
    st.Page("pages/page_simulate.py",  title="Simulate"),
    st.Page("pages/page_storage.py", title="Stored scenarios"),
    st.Page("pages/page_ml_summary.py",  title="Summary"),
    st.Page("pages/page_settings.py",  title="Settings"),
    ]

pg = st.navigation(pages)

pg.run()

with st.sidebar:
    st.markdown(''':primary[QUICK GUIDE]''')
    st.text("(1) Define distributional scenarios")
    st.text("(2) Run simulations")
    st.text("(3) Check the plotted results")
    st.title(""); st.title(""); st.title(""); 
    st.title(""); st.title("")

    # logos an links
    st.header("");st.header("");st.header("")
    st.header("");st.header("");st.header("")
    c1,c2=st.columns([80,200])
    c1.text("")

    st.logo(image='pics/z_logo_violet.png', size="large", link="https://github.com/sergezaugg")