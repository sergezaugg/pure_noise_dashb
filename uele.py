#--------------------             
# Author : Serge Zaugg
# Description : gui elements
#--------------------

import streamlit as st
import plotly.express as px
from streamlit import session_state as ss
from utils import update_ss, plot_scenarios


def select_distr_param():
    with st.container(border=True, key='conta_01', height = 500):
        CA, CB = st.columns([0.65, 0.35])
        with CA:
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
            # ...
            sce_temp = {
                    'n1' : n1, 'mu1' : [mu1x, mu1y] , 'std1' : [std1x, std1y], 'corr1' : corr1,
                    'n2' : n2, 'mu2' : [mu2x, mu2y] , 'std2' : [std2x, std2y], 'corr2' : corr2,
                    }
            # define a name 
            with st.form("f02", border=False, clear_on_submit=True, enter_to_submit=False):
                distr_name = st.text_input(key = "k013", label = "Give a name:", value = "")    
                submitted_1 = st.form_submit_button("Store scenario", type="primary", use_container_width = True)     
                if submitted_1:
                    ss['di_li'][distr_name] = sce_temp

        with CB:
            st.text("Preview")
            fig01 = plot_scenarios(scenarios_di = sce_temp, width = 500, height = 400)
            st.plotly_chart(fig01, use_container_width=False, key='fig01')

      


def select_stored_scenario():
    CA, CB = st.columns([0.50, 0.50])
    with CA:
        _ = st.selectbox('Select', options = ss['di_li'].keys(), key = "wid02", on_change = update_ss, args=["wid02", "par02"])    
    with CB:
        if len(ss["upar"]["par02"]) > 0:
            fig00 = plot_scenarios(scenarios_di = ss['di_li'][ss["upar"]["par02"]], width = 450, height = 450)
            st.plotly_chart(fig00, use_container_width=False, key='fig00')


