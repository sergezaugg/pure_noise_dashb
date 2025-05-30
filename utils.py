#--------------------             
# Author : Serge Zaugg
# Description : Utility and ML functions
#--------------------

import os
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import streamlit as st
from streamlit import session_state as ss


def update_ss(kname, ssname):
    ss["upar"][ssname] = ss[kname]      


def bivariate_normal(n = 1000, mu =[0,0] , std = [3,2], corr = 0.5):
    """ 
    """
    mu = np.array(mu)
    std = np.diag(np.array(std))
    sigma1 = np.array([[1.0,corr],[corr,1.0]])
    xtemp = np.matmul(sigma1, std)
    covar1 = np.matmul(std, xtemp)
    x1 = np.random.multivariate_normal(mean = mu, cov = covar1, size=n)
    return(x1)


# @st.cache_data
def make_dataset(params, n_noisy_features): 
    """  
    """
    # create mvn data with controlled structure
    x1 = bivariate_normal(n = params['n1'], mu = params['mu1'] , std = params['std1'], corr = params['corr1'])
    x2 = bivariate_normal(n = params['n2'], mu = params['mu2'] , std = params['std2'], corr = params['corr2'])
    # add a class for supervised classification
    x1 = pd.DataFrame(x1, columns = ["f01", "f02"])
    x1["class"] = "Class A"
    x2 = pd.DataFrame(x2, columns = ["f01", "f02"])
    x2["class"] = "Class B"
    df = pd.concat([x1, x2])
    # re-order columns nicely 
    column_to_move = df.pop("class")
    df.insert(0, "class", column_to_move)
    df = df.reset_index(drop=True)
    # add multiple features that are uninformative for classification
    rand_feats = np.random.normal(0, 1, n_noisy_features*df.shape[0])
    rand_feats = rand_feats.reshape((df.shape[0], n_noisy_features))
    col_names = ['r'+str(a).zfill(3) for a in range(n_noisy_features)]
    df_rand_feats = pd.DataFrame(rand_feats, columns = col_names)
    df_rand_feats = df_rand_feats.reset_index(drop=True)
    # bring together the 2 informative an all the non-informative features 
    df = pd.concat([df, df_rand_feats], axis = 1)
    return(df)


# @st.cache_data
def evaluate_scenarios_rfo(sce, nb_noisy_features, ntrees, rfo_max_features, test_prop):
    """
    """
    df_resu = []
    mvn_params = sce
    for counter, nb_noisfeat in enumerate(nb_noisy_features):
        # print(nb_noisfeat)
        df = make_dataset(params = mvn_params, n_noisy_features = int(nb_noisfeat)) 
        # select predictors and response 
        X = df.iloc[:,1:]
        y = df['class']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_prop)
        # initialize a model for supervised classification 
        clf = RandomForestClassifier(n_estimators=ntrees, max_depth=30, max_features = rfo_max_features)
        clf.fit(X_train, y_train)
        # get overall performance as ROC-AUC
        y_pred = clf.predict_proba(X_test)[:,1]
        resu_auc = np.round(roc_auc_score(y_test, y_pred),2).item()
        df_t = pd.DataFrame([{"nb_noisy_features": nb_noisfeat, "resu_auc": resu_auc,}])
        df_resu.append(df_t)
    df_final = pd.concat(df_resu)
    # df_final['xxxx'] = ssss
    df_final['model_type'] = 'RFO'
    df_final['rfo_nb_trees'] = ntrees
    df_final['rfo_max_features'] = rfo_max_features
    # keep track 
    diresu = {
        'scenarios_di' : sce,
        'df_result' : df_final
        }
    return(diresu)


@st.cache_data
def plot_scenarios(scenarios_di, colors, width = 450, height = 450, tit_str = "", margin_r=150, margin_t=40):
    """
    """
    # tit_str = 'Class A: N=' + str(scenarios_di['n1']) + '   Class B: N=' + str(scenarios_di['n2'])
    df = make_dataset(params = scenarios_di, n_noisy_features = 0) 
    fig1 = px.scatter(
        data_frame = df,
        x = 'f01',
        y = 'f02',
        color = 'class',
        width = width,
        height = height,
        title = tit_str,
        template="plotly_dark",
        color_discrete_sequence = colors,
        )         
    _ = fig1.update_xaxes(showline = True, linecolor = 'white', linewidth = 2, row = 1, col = 1, mirror = True)
    _ = fig1.update_yaxes(showline = True, linecolor = 'white', linewidth = 2, row = 1, col = 1, mirror = True)
    _ = fig1.update_traces(marker={'size': 2})
    _ = fig1.update_layout(paper_bgcolor="#002240")
    _ = fig1.update_layout(margin=dict(r=margin_r, t=margin_t ))
    _ = fig1.update_layout(legend=dict(yanchor="top", y=0.9, xanchor="left", x=1.1)) 
    # fig1.show()
    return(fig1)    




# devel 
if __name__ == "__main__":

    xx = bivariate_normal(n = 1000, mu =[1,1] , std = [1,1], corr = -0.9)
    xx.shape
    xx.std(0)
    pd.DataFrame(xx).corr()

    params = {
        'n1' : 100, 'mu1' : [0,0] , 'std1' : [1,1], 'corr1' : -0.9,
        'n2' : 100, 'mu2' : [0,0] , 'std2' : [1,1], 'corr2' : -0.9,
        }

    df = make_dataset(params = params, n_noisy_features = 1000) 

    df.head()
    df.shape

    "{:1.2f}".format(456.67895) # check 

