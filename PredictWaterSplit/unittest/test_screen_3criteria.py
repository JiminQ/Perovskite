
# coding: utf-8

# In[ ]:


import screen_3criteria
import open_database
import pandas as pd
import numpy as np


def test_screen_3criteria():
    perovskite,values,data_total=open_database.read_database()
    screening2=screen_3criteria.screening(data_total)
    np.testing.assert_almost_equal(screening2.iloc[0,:]['VB_dir'],5.861354) 
    np.testing.assert_almost_equal(screening2.iloc[0,:]['gllbsc_dir_gap'],1.4)
    
    return

