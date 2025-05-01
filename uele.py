#--------------------             
# Author : Serge Zaugg
# Description : gui elements
#--------------------

import streamlit as st
import plotly.express as px
from streamlit import session_state as ss
import numpy as np
import pandas as pd
from utils import update_ss, plot_scenarios, evaluate_scenarios_rfo


def select_distr_param():
    with st.expander("(1) Define a scenario (click to expand/collapse)", expanded=True):
        CA, CB, CC = st.columns([0.60, 0.05, 0.30])
        with CA:
            # 
            c0, c1, c2, c3, c4, c5, c6, = st.columns(7) 
            c0.text("Class A")
            n1 = c1.number_input(label = "N",  min_value=10, max_value=10000,               value=ss['distr']['n1'],      step=100, key = "k001")
            mu1x = c2.number_input(label = "Mean X", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu1'][0],  step=1.0, key = "k002")
            mu1y = c3.number_input(label = "Mean Y", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu1'][1],  step=1.0, key = "k003")
            std1x = c4.number_input(label = "Stdev X", min_value=0.01, max_value=10.0,      value=ss['distr']['std1'][0], step=0.1, key = "k004")
            std1y = c5.number_input(label = "Stdev Y", min_value=0.01, max_value=10.0,      value=ss['distr']['std1'][1], step=0.1, key = "k005")
            corr1 = c6.number_input(label = "Correlation", min_value=-1.0, max_value=+1.0,  value=ss['distr']['corr1'],   step=0.05, key = "k006")
            # 
            c0, c1, c2, c3, c4, c5, c6, = st.columns(7)
            c0.text("Class B")
            n2 = c1.number_input(label = "N",  min_value=10, max_value=10000,               value=ss['distr']['n2'],      step=100, key = "k007")
            mu2x = c2.number_input(label = "Mean X", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu2'][0],  step=1.0, key = "k008")
            mu2y = c3.number_input(label = "Mean Y", min_value=-10.0, max_value=10.0,       value=ss['distr']['mu2'][1],  step=1.0, key = "k009")
            std2x = c4.number_input(label = "Stdev X", min_value=0.01, max_value=10.0,      value=ss['distr']['std2'][0], step=0.1, key = "k010")
            std2y = c5.number_input(label = "Stdev Y", min_value=0.01, max_value=10.0,      value=ss['distr']['std2'][1], step=0.1, key = "k011")
            corr2 = c6.number_input(label = "Correlation", min_value=-1.0, max_value=+1.0,  value=ss['distr']['corr2'],   step=0.05, key = "k012")
            # ...
            sce_temp = {
                    'n1' : n1, 'mu1' : [mu1x, mu1y] , 'std1' : [std1x, std1y], 'corr1' : corr1,
                    'n2' : n2, 'mu2' : [mu2x, mu2y] , 'std2' : [std2x, std2y], 'corr2' : corr2,
                    }
            # define a name 
            with st.form("f02", border=False, clear_on_submit=True, enter_to_submit=False):
                c1, c2, c3 = st.columns(3)  
                with c1:
                    distr_name = st.text_input(key = "k013", label = "Give a name:", value = "") 
                with c2: 
                    st.text("") 
                    st.text("")   
                    submitted_1 = st.form_submit_button("Store scenario", type="primary", use_container_width = False)  
                    if len(distr_name) < 3:
                        st.text("Name must contain at least 3 charters")  
                    else:    
                        if submitted_1:
                            ss['di_li'][distr_name] = sce_temp
                            # delete initial key 
                            ss['di_li'].pop("Please create a scenario", None)
                            ss["upar"]["par02"] = distr_name
                            # get numerical index of newly created scenario name 
                            ss['num_index_sce'] = np.where([a==distr_name for a in ss['di_li'].keys()])[0].item()

        with CB:
            st.text("Preview:")
        with CC:
            fig01 = plot_scenarios(scenarios_di = sce_temp, width = 450, height = 350)
            st.plotly_chart(fig01, use_container_width=False, key='fig01')

      


def select_stored_scenario():
    with st.expander("(2) Run simulations (click to expand/collapse)", expanded=True):
        CA, _, CB, CC = st.columns([0.45, 0.15, 0.05, 0.30])
        with CA:
            coa, cob = st.columns([0.50, 0.50])
            _ = coa.selectbox('Select a scenario', index=ss['num_index_sce'], options = ss['di_li'].keys(), key = "wid02", on_change = update_ss, args=["wid02", "par02"])  

            if not ss["upar"]["par02"] == 'initial': # len(ss["upar"]["par02"]) > 0:
                nnoi_ops = 2**np.arange(0,13,1)
                _ = st.segmented_control("Nb noisy features", options=nnoi_ops, selection_mode="multi", 
                                         default = ss["upar"]["par03"],  key="wid03", on_change=update_ss, args=["wid03", "par03"],)
                coa, cob = st.columns([0.50, 0.50])
                _ = coa.select_slider("RFO max features", options=np.arange(1,31,1), value=ss["upar"]["par04"], key="wid04", on_change=update_ss, args=["wid04", "par04"],)
                _ = cob.slider("RFO n trees", min_value=1, max_value=30, value=ss["upar"]["par05"], step=1, key="wid05", on_change=update_ss, args=["wid05", "par05"],)
                                
                with st.form("f03", border=False, clear_on_submit=True, enter_to_submit=False):
                    coa, cob = st.columns([0.20, 0.50])
                    message01 = "New dataset sampled from scenario at each run to create Monte-Carlo replicates of same scenario"
                    submitted3 = coa.form_submit_button("Start simulation", type="primary", use_container_width = False, help=message01) 
                    if submitted3:
                        resu01 = evaluate_scenarios_rfo(sce = ss['di_li'][ss["upar"]["par02"]], 
                            nb_noisy_features = ss["upar"]["par03"],  
                            rfo_max_features = ss["upar"]["par04"], 
                            ntrees = ss["upar"]["par05"], 
                            )
                        # include some metadata and scenario
                        df = resu01['df_result']
                        df['scenario'] = ss["upar"]["par02"]
                        df['run_nb'] = ss['run_nb']
                        ss['run_nb'] += 1
                        ss['resu'].append(df)
        with CB:
            st.text("Selected")
        with CC:
            if not ss["upar"]["par02"] == 'initial': # len(ss["upar"]["par02"]) > 0:
                fig00 = plot_scenarios(scenarios_di = ss['di_li'][ss["upar"]["par02"]], width = 450, height = 350, tit_str = ss["upar"]["par02"])
                st.plotly_chart(fig00, use_container_width=False, key='fig00')


@st.cache_data
def prepare_results(li):
    """
    li : a list of dataframes 
    """
    df = pd.concat(li)
    df = df.sort_values(by = [ 'rfo_max_features', 'nb_noisy_features', 'scenario', 'run_nb'])
    return(df)


@st.cache_data
def make_plot(df, width, height):
    with st.expander("(3) Check simulation results (click to expand/collapse)", expanded=True):
        plotcol_seq02 = ['#ff0000', '#ffff66', '#33ff00', '#00ffff', '#ffbb00', '#ff00ff', '#0077ff',]
        fig03 = px.line(
            data_frame = df,
            x = 'nb_noisy_features',
            y = 'resu_auc',
            color = 'scenario',
            line_group = 'run_nb',
            facet_col = 'rfo_max_features',
            facet_row = 'rfo_nb_trees',
            facet_row_spacing = 0.1, 
            facet_col_spacing = 0.05,
            width = width,
            height = height,
            markers = True,
            template = "plotly_dark",
            log_x = True, 
            color_discrete_sequence = plotcol_seq02,
            )
        _ = fig03.update_layout(paper_bgcolor="#002240")
        _ = fig03.update_layout(yaxis_range=[0.4,1.05])
        st.plotly_chart(fig03, use_container_width=False, key='fig03')



