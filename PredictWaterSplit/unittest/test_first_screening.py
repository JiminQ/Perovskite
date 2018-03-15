
# coding: utf-8

# In[ ]:


import pandas as pd
import open_database
import screen_3criteria as sc
import numpy as np
import first_screening as fs

def test_first_screening():
    perovskite,values,data_total=open_database.read_database() #3 dataframe
    screening_data=sc.screening(data_total) #23 data after screening
    your_data,comment=fs.input_screening(A_ion='Ca',B_ion='Nb',anion='O2N',mass=178.99,volume=68.3331)
    assert type(your_data)==pd.DataFrame, "Data type error"
    assert your_data.iloc[0,:]['anion_IE']==13.92342, "Get your_data feature error"
    assert comment == "Yes,it can do water-slpitting", "Comment on its water-splitting ability error"

    return

