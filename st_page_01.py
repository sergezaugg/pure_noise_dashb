#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit import session_state as ss
from uele import select_distr_param, select_stored_scenario
from utils import update_ss, plot_scenarios , evaluate_scenarios_rfo




select_distr_param()

select_stored_scenario()



if len(ss["upar"]["par02"]) > 0:
    nnoi_ops =  [1, 3, 5, 10, 30, 100, 300, 1000]
    _ = st.segmented_control("Nb noisy features", options=nnoi_ops, selection_mode="multi", key="wid03", on_change=update_ss, args=["wid03", "par03"],)
    max_feat_ops = [1,2,3,4,5,6,7,8,9]
    _ = st.select_slider("RFO max features", options=max_feat_ops, value=2, key="wid04", on_change=update_ss, args=["wid04", "par04"],)
                     
    with st.form("f03", border=False, clear_on_submit=True, enter_to_submit=False):
        submitted3 = st.form_submit_button("Start simulation", type="primary", use_container_width = True)  
        if submitted3:
            resu01 = evaluate_scenarios_rfo(sce = ss['di_li'][ss["upar"]["par02"]], 
                nb_noisy_features = ss["upar"]["par03"],  
                ntrees = 10, 
                rfo_max_features = ss["upar"]["par04"], 
                )
            # include som metadata and scenario
            df = resu01['df_result']
            df['scenario'] = ss["upar"]["par02"]
            df['run_nb'] = ss['run_nb']
            ss['run_nb'] += 1
            ss['resu'].append(df)





df_out = pd.concat(ss['resu'])
print(df_out)
# st.write(df_out)
df_out = df_out.sort_values(by = [ 'rfo_max_features', 'nb_noisy_features', 'scenario', 'run_nb',  ])



# nb_noisy_features  resu_auc model_type  rfo_nb_trees  rfo_max_features  scenario
fig03 = px.line(
    data_frame = df_out,
    x = 'nb_noisy_features',
    y = 'resu_auc',
    # 
    color = 'scenario',
    line_group = 'run_nb',
    facet_col = 'rfo_max_features',
    width = 900,
    height = 600,
    markers=True,
    title = "",
    template="plotly_dark",
    log_x = True,
    # color_discrete_sequence = plotcol_seq02,
    )


st.plotly_chart(fig03, use_container_width=False, key='fig03')


with st.container(height=700, border=True):
    st.text("Session state's internal values") 
    for k in st.session_state:
        st.write(k, st.session_state[k])



