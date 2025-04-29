#--------------------             
# Author : Serge Zaugg
# Description : Create datasets, train models, assess performance
#--------------------

from utils import evaluate_scenarios_rfo, plot_scenarios
import os

# random_seed = 557
path_save_figures = "./saved_figures_temp"
N = 3000

# Define  scenarios 
sce01 = { 
        'n1' : N, 'mu1' : [0.0, 2.0] , 'std1' : [1.1,1.1], 'corr1' : 0.00,
        'n2' : N, 'mu2' : [2.0, 0.0] , 'std2' : [1.0,1.0], 'corr2' : 0.00,
        }
 

sce02 = { 
        'n1' : N, 'mu1' : [0.0, 1.0] , 'std1' : [1.1,1.1], 'corr1' : 0.90,
        'n2' : N, 'mu2' : [2.0, 0.0] , 'std2' : [1.0,1.0], 'corr2' : 0.90,
        }


scedi  = {}


sce_nam01 = "blabla"

scedi[sce_nam01] = sce01

sce_nam02 = "clouclou"

scedi[sce_nam02] = sce02

scedi.keys()




fig00 = plot_scenarios(scenarios_di = scedi[sce_nam02], width = 450, height = 450)
fig00.show()




nb_noisy_features = [0, 1, 5, 10, 50, 100]
nb_trees = 10

resu01 = evaluate_scenarios_rfo(sce = scedi[sce_nam02], nb_noisy_features = nb_noisy_features,  ntrees = nb_trees, rfo_max_features = 1)


nb_noisy_features = [0, 1, 10, 50,]
nb_trees = 11

resu02 = evaluate_scenarios_rfo(sce = scedi[sce_nam02], nb_noisy_features = nb_noisy_features,  ntrees = nb_trees, rfo_max_features = 5)


resu01['scenarios_di']

resu01['df_result']

resu01['df_result'].shape
resu02['df_result'].shape






