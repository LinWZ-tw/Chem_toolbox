# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:01:38 2021
@author: lin, wei-zhi
"""
"""
# input by user, an example was entered
comp_list = ['amitriptyline','tranylcypromine','mianserin','triflupromazine','doxylamine','protriptyline','metixene','citalopram','benserazide', 'acepromazine']
"""
def sortSMILE (comp_list):
    import pandas as pd    # import statement
    treatment_info = pd.read_csv('https://ndownloader.figshare.com/files/20237715')     # PRISM 19Q4 primary-screen-replicate-collapsed-treatment-info.csv
    treatment_info = treatment_info[['name', 'smiles']]    # trim treatment info
    treatment_info['smiles'] = treatment_info['smiles'].str.split(",").str.get(0)
    comp_df = pd.DataFrame(comp_list)    # select compunds of interest
    comp_df = comp_df.rename(columns={0:'name'})
    sort_smiles = pd.merge(treatment_info, comp_df, left_on='name', right_on = 'name')
    comp_smile_dic = sort_smiles.set_index('name').T.to_dict('list')
    print (comp_smile_dic)
    return comp_smile_dic
"""
#%% test
sortSMILE (comp_list)
"""
