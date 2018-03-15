import pandas as pd
import numpy
import open_database
import predictbyKRR
import featureselect
import outlier
from sklearn.kernel_ridge import KernelRidge


perovskite,values,data_total = open_database.read_database()
traindata,testdata = predictbyKRR.build_data(data_total)

def test_build_data():
    traindata,testdata = predictbyKRR.build_data(data_total)
    assert list(traindata.columns) == list(testdata.columns),'train test data not match'
    return

def test_krr_predict():
    feature_list = ['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_aff', 'B_IE', 'B_aff', 'volume', 'mass', 'A_R', 'B_R', 'aff_A+B', 'aff_A-B', 'A_R_max', 'B_R_max']
    krr = KernelRidge(alpha=1., kernel='polynomial',degree = 4)
    predict_train, predict_test, mse_test, Rsquared_test, mse_train, Rsquared_train= predictbyKRR.krr_predict(feature_list,krr,traindata,testdata,'CB_ind')
    assert Rsquared_test<=1. and Rsquared_train<=1.,'Wrong R squared scale'
    assert mse_test<=1. and mse_train<=1.,'Wrong MSE scale'
    assert len(predict_train)==len(traindata),'predict and true data not match'
    assert len(predict_test)==len(testdata),'predict and true data not match'
    assert type(predict_train)==numpy.ndarray,'Wrong predict type of train'
    assert type(predict_test)==numpy.ndarray,'Wrong predict type of test'
    return

def test_predict_Band():
    feature_list = ['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_aff', 'B_IE', 'B_aff', 'volume', 'mass', 'A_R', 'B_R', 'aff_A+B', 'aff_A-B', 'A_R_max', 'B_R_max']
    predict_train,predict_test = predictbyKRR.predict_Band(feature_list,traindata,testdata,'CB_dir')
    assert len(predict_train)==len(traindata),'predict and true data not match'
    assert len(predict_test)==len(testdata),'predict and true data not match'
    assert type(predict_train)==numpy.ndarray,'Wrong predict type of train'
    assert type(predict_test)==numpy.ndarray,'Wrong predict type of test'
    return

def test_feature_select():
    least_corr_list = featureselect.feature_select(perovskite,26)
    assert type(least_corr_list)==pd.core.frame.DataFrame,'Wrong corr list type'
    for i in range(0,4):
        assert least_corr_list.iloc[i]['sum of correlation']<least_corr_list.iloc[i+1]['sum of correlation'],'Wrong corr list'
    return