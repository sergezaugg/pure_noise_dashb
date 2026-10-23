#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
from streamlit import session_state as ss
from utils import update_ss

st.text("Scatter color")
cols_a = st.columns(18)
ss["upar"]["col_a"] = cols_a[0].color_picker("Class A", ss["upar"]["col_a"])   
ss["upar"]["col_b"] = cols_a[1].color_picker("Class B", ss["upar"]["col_b"])  

st.text("  ")  
st.text("Line color")  
cols_b = st.columns(18)   
ss["upar"]["col_seq"][0] = cols_b[0].color_picker("Class 0", ss["upar"]["col_seq"][0])   
ss["upar"]["col_seq"][1] = cols_b[1].color_picker("Class 1", ss["upar"]["col_seq"][1])   
ss["upar"]["col_seq"][2] = cols_b[2].color_picker("Class 2", ss["upar"]["col_seq"][2])   
ss["upar"]["col_seq"][3] = cols_b[3].color_picker("Class 3", ss["upar"]["col_seq"][3])   
ss["upar"]["col_seq"][4] = cols_b[4].color_picker("Class 4", ss["upar"]["col_seq"][4])   
ss["upar"]["col_seq"][5] = cols_b[5].color_picker("Class 5", ss["upar"]["col_seq"][5])   
ss["upar"]["col_seq"][6] = cols_b[6].color_picker("Class 6", ss["upar"]["col_seq"][6])   

st.text("  ")  
st.text("  ")  
cols_c = st.columns(5)   
_ = cols_c[0].slider("Test set size (proportion)", min_value=0.05, max_value=0.95, label_visibility = "visible",
              value=ss["upar"]["test_size_prop"], key="wid_testset", on_change=update_ss, args=["wid_testset", "test_size_prop"],)
