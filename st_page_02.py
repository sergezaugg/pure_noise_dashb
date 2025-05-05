#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st

col_a, col_space01 = st.columns([0.60, 0.25])

with col_a:

    with st.container(border=True, key='conta_01'):
        st.title(":blue[Impact of pure-noise-features on predictive performance]") 
        st.page_link("st_page_01.py", label="LINK : Interactive dashboard")

    st.markdown('''   
    In the top tab you can define multiple distributional scenarios for two classes and store each with a custom name.
    There is a preview left to finetune the distribution before storing them.
    The second tab allow to
    (1) choose one of the stored scenario,
    (2) choose the range of pure-noise-features to include into the feature space, and
    (3) choose the Random Forest parameters.
    Then you can start a simulation with the above parameters.
    At each run, the dataset will be split 50/50 into train and test set.
    The simulation results are accumulated in memory and shown in the two bottom tabs.
    Note tha each time you run a simulation a new dataset is randomly sampled from the scenario.
    Thus you can do multiple Monte-Carlo replicates (recommended).
    ''')

    st.image("pics/pic01.png")

    st.markdown('''   
    In the two bottom tabs you can see the simulation results and one realization of each scenario.
    The classification performance is given as the ROC-AUC and plotted against the number of pure-noise-features.
    These are Plotly plots, thus you can zoom and all axes will remain comparable.
    In this example, 3 scenarios were compared for two sets of RF parameters.
    We can see that the linearly-separable scenario (red) was more robust to pure-noise-features than the cross scenario (yellow).
    We also see that for the cat-eye scenario (green), the RF with max-feature = 1 collapses already with 10 pure-noise-features.
    As expected, raising max-feature to 10 considerably improved the robustness to pure-noise-features.
    Caution, these results do not directly translate to real-world datasets.
    But it is interesting to see that in certain situations, RF can handle dozens of pure-noise-features with almost no loss in predictive performance.
    Have fun an try it yourself with new scenarios!                        
    ''')

    st.image("pics/pic02.png")


   

    # st.divider()



