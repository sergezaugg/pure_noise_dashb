#--------------------             
# Author : Serge Zaugg
# Description : gui elements
#--------------------

import streamlit as st
import plotly.express as px
from streamlit import session_state as ss


def select_distr_param():
    with st.form("f02", border=False, clear_on_submit=False, enter_to_submit=False):
        with st.container(border=True, key='conta_01', height = 400):
            st.text("Define distribution class A")
            c1, c2, c3, c4, c5, c6, = st.columns(6)  
            with c1:
                n1 = st.number_input(label = "N",  min_value=10, max_value=10000,               value=ss['distr']['n1'],      step=100, key = "k001")
            with c2:
                mu1x = st.number_input(label = "Mean X", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu1'][0],  step=1.0, key = "k002")
            with c3:
                mu1y = st.number_input(label = "Mean Y", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu1'][1],  step=1.0, key = "k003")
            with c4:
                std1x = st.number_input(label = "Stdev X", min_value=0.01, max_value=10.0,      value=ss['distr']['std1'][0], step=0.1, key = "k004")
            with c5:
                std1y = st.number_input(label = "Stdev Y", min_value=0.01, max_value=10.0,      value=ss['distr']['std1'][1], step=0.1, key = "k005")
            with c6:
                corr1 = st.number_input(label = "Correlation", min_value=-1.0, max_value=+1.0,  value=ss['distr']['corr1'],   step=0.1, key = "k006")
            st.text("Define distribution class B")
            c1, c2, c3, c4, c5, c6, = st.columns(6)
            with c1:
                n2 = st.number_input(label = "N",  min_value=10, max_value=10000,               value=ss['distr']['n2'],      step=100, key = "k007")
            with c2:
                mu2x = st.number_input(label = "Mean X", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu2'][0],  step=1.0, key = "k008")
            with c3:
                mu2y = st.number_input(label = "Mean Y", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu2'][1],  step=1.0, key = "k009")
            with c4:
                std2x = st.number_input(label = "Stdev X", min_value=0.01, max_value=10.0,      value=ss['distr']['std2'][0], step=0.1, key = "k010")
            with c5:
                std2y = st.number_input(label = "Stdev Y", min_value=0.01, max_value=10.0,      value=ss['distr']['std2'][1], step=0.1, key = "k011")
            with c6:
                corr2 = st.number_input(label = "Correlation", min_value=-1.0, max_value=+1.0,  value=ss['distr']['corr2'],   step=0.1, key = "k012")
            # define a name 
            distr_name = st.text_input(key = "k013", label = "Give a name:", value = "")    
            submitted_1 = st.form_submit_button("Submit values", type="primary", use_container_width = True) 
            if submitted_1:
                print(22)
                ss['di_li'][distr_name] = {
                    'n1' : n1, 'mu1' : [mu1x, mu1y] , 'std1' : [std1x, std1y], 'corr1' : corr1,
                    'n2' : n2, 'mu2' : [mu2x, mu2y] , 'std2' : [std2x, std2y], 'corr2' : corr2,
                    }
                # st.rerun() 





