#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# Run locally : streamlit run stmain.py
#--------------------

import streamlit as st
from streamlit import session_state as ss

st.set_page_config(layout="wide")


init_distr =  {
                'n1' : 200, 'mu1' : [0.0, 0.0] , 'std1' : [1.0, 1.0], 'corr1' : 0.5,
                'n2' : 200, 'mu2' : [0.0, 0.0] , 'std2' : [1.0, 1.0], 'corr2' : -0.5,
                }

if 'distr' not in ss:
    ss['distr'] = init_distr


if 'di_li' not in ss:
    ss['di_li'] = {}



# initial value of session state
if 'upar' not in ss:
    ss["upar"] = {
        "par01" : 1000,
        "par02" : 2,
        "par03" : 0.20, 
        }





















pages = [
    st.Page("st_page_01.py", title="Interactive"),
    # st.Page("st_page_00.py", title="Summary"),
    ]

pg = st.navigation(pages)

pg.run()

with st.sidebar:
    st.text("v1.1.x - improvements underway")
    st.title(""); st.title(""); st.title(""); st.title(""); st.title(""); st.title(""); st.title("")
    st.title(""); st.title(""); st.title(""); st.title("") 
    st.markdown(''':gray[RELATED TOPICS]''')
    st.page_link("https://ml-performance-metrics.streamlit.app/", label=":gray[ml-performance-metrics]")
    st.page_link("https://featureimportance.streamlit.app/", label=":gray[feature-importance:red]")
