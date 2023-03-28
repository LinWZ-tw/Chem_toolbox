# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 00:29:59 2021
@author: lin, wei-zhi
"""
"""
# input by user, an example was entered
comp_list = ['amitriptyline','tranylcypromine','mianserin','triflupromazine','doxylamine','protriptyline','metixene','citalopram','benserazide', 'acepromazine']
comp_smile_dic ={'amitriptyline':'CN(C)CCC=C1c2ccccc2CCc2ccccc12',
                'tranylcypromine':'N[C@H]1C[C@@H]1c1ccccc1',
                'mianserin':'CN1CCN2C(C1)c1ccccc1Cc1ccccc21',
                'triflupromazine':'CN(C)CCCN1c2ccccc2Sc2ccc(cc12)C(F)(F)F',
                'doxylamine':'CN(C)CCOC(C)(c1ccccc1)c1ccccn1',
                'protriptyline':'CNCCCC1c2ccccc2C=Cc2ccccc12',
                'metixene':'CN1CCCC(CC2c3ccccc3Sc3ccccc23)C1',
                'citalopram':'CN(C)CCCC1(OCc2cc(ccc12)C#N)c1ccc(F)cc1',
                'benserazide':'NC(CO)C(=O)NNCc1ccc(O)c(O)c1O',
                'acepromazine':'CN(C)CCCN1c2ccccc2Sc2ccc(cc12)C(C)=O'}
"""
#%% def function
def CSmatrix (comp_list, comp_smile_dic):
    from rdkit import Chem,DataStructs     #import statement
    import pandas as pd
    list_len = len (comp_list)
    data = pd.DataFrame(columns=[comp_list],index=comp_list) #creat a empty df
    for i in range (list_len): #creat score
        for j in range (i,list_len):
            mol1 = Chem.MolFromSmiles(comp_smile_dic[comp_list[i]])
            mol2 = Chem.MolFromSmiles(comp_smile_dic[comp_list[j]])
            fp1 = Chem.RDKFingerprint(mol1)
            fp2 = Chem.RDKFingerprint(mol2)
            score = DataStructs.TanimotoSimilarity(fp1,fp2)
            #fill the df with score
            data.loc[comp_list[i], comp_list[j]] = score
            data.loc[comp_list[j], comp_list[i]] = score
    data.to_excel('CompoundSimilarityMatrix.xlsx')     #output data
    return data
"""
# test
print (CSmatrix(comp_list, comp_smile_dic))
"""
