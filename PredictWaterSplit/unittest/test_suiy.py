
# coding: utf-8

# In[ ]:

import prediction_watersplitting
import open_database
import numpy as np 

def test_sui_ANN():
    perovskite,values,data_total=open_database.read_database()
    test_data = data_total.loc[0:1]
    prediction_watersplitting.model()
    result4=prediction_watersplitting.prediction_on_dir_VB(data_total,test_data)
    result5=0.7*data_total.loc[1]['VB_dir']
    result6=1.3*data_total.loc[1]['VB_dir']
    assert result4>result5 and result4<result6,"result error"
    
    prediction_watersplitting.model()
    result7=prediction_watersplitting.prediction_on_dir_CB(data_total,test_data)
    result8=0.9*data_total.loc[1]['CB_dir']
    result9=1.1*data_total.loc[1]['CB_dir']
    assert result7>result8 and result7<result9,"result error"
    
    prediction_watersplitting.model()
    result1=prediction_watersplitting.prediction_hof(data_total,test_data)
    result2=0.7*data_total.loc[1]['heat_of_formation']
    result3=1.3*data_total.loc[1]['heat_of_formation']
    assert result1>result2 and result1<result3,"result error"
    
    prediction_watersplitting.model()
    result10=prediction_watersplitting.prediction_on_indir_VB(data_total,test_data)
    result11=0.9*data_total.loc[1]['VB_ind']
    result12=1.1*data_total.loc[1]['VB_ind']
    assert result10>result11 and result10<result12,"result error"
    
    prediction_watersplitting.model()
    result13=prediction_watersplitting.prediction_on_indir_CB(data_total,test_data)
    result14=0.9*data_total.loc[1]['CB_ind']
    result15=1.1*data_total.loc[1]['CB_ind']
    assert result13>result14 and result13<result15,"result error"
    return

