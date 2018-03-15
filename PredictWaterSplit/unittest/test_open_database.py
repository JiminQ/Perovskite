
# coding: utf-8

# In[ ]:


import open_database
import pandas as pd
import numpy as np


def test_opendatabase():
    perovskite,values,data_total=open_database.read_database()
    assert type(perovskite)==pd.DataFrame, "Data type error"
    assert type(values)==pd.DataFrame, "Data type error"
    assert type(data_total)==pd.DataFrame, "Data type error"
    
    assert values.iloc[0,:]['CB_ind'] > 0.0, "Screening CB_ind error"
    np.testing.assert_almost_equal(perovskite.iloc[0,:]['X_A+B'],3.72)
    np.testing.assert_almost_equal(perovskite.iloc[0,:]['anion_X'],3.30666)
    np.testing.assert_almost_equal(values.iloc[0,:]['CB_ind'],5.96271244252951)
    np.testing.assert_almost_equal(data_total.iloc[0,:]['A_s_R'],162.2)
    
    return
    

