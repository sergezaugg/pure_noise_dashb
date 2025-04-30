#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# Run locally : streamlit run stmain.py
#--------------------

import streamlit as st
from streamlit import session_state as ss
from utils import update_ss
st.set_page_config(layout="wide")

init_distr =  {
    'n1' : 2000, 'mu1' : [0.0, 0.0] , 'std1' : [1.0, 1.0], 'corr1' : 0.5,
    'n2' : 2000, 'mu2' : [0.0, 0.0] , 'std2' : [1.0, 1.0], 'corr2' : -0.5,
    }

if 'distr' not in ss:
    ss['distr'] = init_distr

if 'di_li' not in ss:
    ss['di_li'] = {}
    ss['di_li']['empty'] = {}

if 'upar' not in ss:
    ss["upar"] = {
        "par01" : 1000,
        "par02" : {},
        "par03" : [1,10,100,1000], 
        "par04" : 1, 
        "par05" : 10, 
        "par10" : 500, 
        "par11" : 500, 
        }

if 'resu' not in ss:
    ss['resu'] = []

if 'dfresu' not in ss:
    ss['dfresu'] = []

if 'run_nb' not in ss:
    ss['run_nb'] = 0



pages = [
    st.Page("st_page_01.py", title="Interactive"),
    st.Page("st_page_00.py", title="Summary"),
    ]

pg = st.navigation(pages)

pg.run()

with st.sidebar:
    st.text("v0.0.0 - bla")

    st.title(""); 

    _ = st.slider("plot width",  min_value=100, max_value=2000, value=500, step=100, key="wid10", on_change=update_ss, args=["wid10", "par10"])
    _ = st.slider("plot height", min_value=100, max_value=2000, value=500, step=100, key="wid11", on_change=update_ss, args=["wid11", "par11"])


    st.title(""); st.title(""); st.title(""); st.title(""); st.title(""); st.title("")
    st.title(""); st.title(""); st.title(""); st.title("") 
    st.markdown(''':gray[RELATED TOPICS]''')
    st.page_link("https://ml-performance-metrics.streamlit.app/", label=":gray[ml-performance-metrics]")
    st.page_link("https://featureimportance.streamlit.app/", label=":gray[feature-importance:red]")
