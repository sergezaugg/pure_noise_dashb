#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
# following supported colors: blue, green, orange, red, violet, gray/grey, rainbow, or primary. 
#--------------------

import streamlit as st

col_a, col_space01 = st.columns([0.50, 0.50])

with col_a:

    with st.container(border=True, key='conta_01'):
        st.title(":blue[Impact of pure-noise-features on predictive performance]") 
        st.subheader(":blue[Applied Machine Learning  ---  ML Tutorials  ---  Supervised Classification]") 
        st.page_link("st_page_01.py", label="LINK : Interactive dashboard")

    st.markdown('''   
    :blue[**INTRODUCTION**]
    
    In supervised classification applications, many features are often available but not all may be needed.
    Detecting and excluding non-informative features if less trivial than it seems.
    It is therefore legitimate to ask which amount of non-informative features is acceptable. 
    This mini-project gives some answers based on simulated data.    
    ''')

    st.markdown(''' 
    :blue[**METHODS**]
                            
    A binary class variable and two features that inform classification are created.
    Many additional pure-noise-features can be included in the feature space.
    They are non-informative for the classification task because they are sampled from the same random normal for both classes.
    Classifiers are trained on this data and their predictive performance (ROC-AUC) is computed (50% train/test split).
    As a primary modeling method, the Random Forest was chosen because it can handle non-linear problems, it is robust to feature scale, and its hyper-parameters are easy to tune.
    Random Forest has one important hyper-parameter, **max_features**, which is the number of features to consider during search of best split. 
    ''')

    st.divider()



# st.text("debugging info")
# with st.container(height=700, border=True):
#     st.text("Session state's internal values") 
#     for k in st.session_state:
#         st.write(k, st.session_state[k])



