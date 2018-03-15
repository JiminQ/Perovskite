
# coding: utf-8

# ### Screening on 19000+data after importing open_database:

# In[1]:


def screening(data_total):
    E0=-4.5
    screening1=data_total[(data_total.gllbsc_ind_gap >= 1.4) & (data_total.gllbsc_ind_gap <= 3.1)& (data_total.CB_ind <= 0 - E0) & (data_total.VB_ind >= 1.23 - E0) | (data_total.gllbsc_dir_gap >= 1.4) & (data_total.gllbsc_dir_gap <= 3.1) & (data_total.CB_dir <= 0 - E0) & (data_total.VB_dir >= 1.23 - E0)]
    screening2=screening1[(screening1.heat_of_formation<=0.21)]
    
    return screening2 #23data

