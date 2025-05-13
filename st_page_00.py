#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st

col_a, col_space01 = st.columns([0.60, 0.40])

with col_a:

    with st.container(border=True):
        st.title(":blue[Impact of pure-noise-features on predictive performance]") 
        st.page_link("st_page_01.py", label="LINK : Interactive dashboard")

    st.markdown('''   
    :blue[**INTRODUCTION**]
    
    In supervised classification applications, many features are often available but not all may be needed.
    Detecting and excluding non-informative features is less trivial than it seems.
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

    st.markdown(''' 
    :blue[**DETAILED GUIDE**]''')

    st.markdown('''   
    In the top tab you can define multiple distributional scenarios for two classes and store each with a custom name.
    There is a preview shown on the left to visually check the distribution before storing.
    The second tab allow to
    (1) choose one of the stored scenario,
    (2) choose the range of pure-noise-features to include into the feature space, and
    (3) choose the Random Forest parameters.
    Then you can start a simulation with the provided parameters.
    At each run, the dataset will be split 50/50 into train and test set.
    The simulation results are accumulated in memory and shown in the two bottom tabs.
    Note that each time you run a simulation a new dataset is randomly sampled from the scenario.
    Thus you can do multiple Monte-Carlo replicates (recommended).
    ''')

    st.image("pics/pic01.png")

    st.markdown('''   
    In the third tabs you can see the simulation results and in the fourth (bottom) a realization of each scenario.
    The classification performance is given as the ROC-AUC and plotted against the number of pure-noise-features.
    These are Plotly plots, thus you can zoom and all axes will remain comparable.
    In this example, 3 scenarios were compared for two sets of RF parameters.
    We can see that the linearly-separable scenario (red) was more robust to pure-noise-features than the cross scenario (yellow).
    We also see that for the cat-eye scenario (green), the RF with max-feature = 1 collapses already with 10 pure-noise-features.
    As expected, raising max-feature considerably improved the robustness to pure-noise-features.
    Caution, these results do not directly translate to real-world datasets.
    But it is interesting to see that in certain situations, RF can handle dozens of pure-noise-features with almost no loss in predictive performance.
    Have fun an try it yourself with new scenarios!                        
    ''')

    st.image("pics/pic03.png")
    st.image("pics/pic04.png") 
    st.divider()





# st.text("debugging info")
# with st.container(height=700, border=True):
#     st.text("Session state's internal values") 
#     for k in st.session_state:
#         st.write(k, st.session_state[k])



