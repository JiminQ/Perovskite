import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
#%matplotlib inline

import numpy as np

def build_data(data_total):
    seed = 21899
    traindata,testdata = train_test_split(data_total,test_size=0.20,random_state=seed)
    return traindata,testdata


def krr_predict(feature_list,krr,traindata,testdata,which):
    # n is the number of features that you want to use in KRR
    # norm=1 means do the normalization of x_train and y_train data
    y_train = traindata[which]
    y_test = testdata[which]
    x_train = [0.]*len(feature_list)
    x_test = [0.]*len(feature_list)
    for i in range(len(feature_list)):
        x_train[i] = traindata[feature_list[i]]
        x_test[i] = testdata[feature_list[i]]
    x_train = np.transpose(x_train)
    x_test = np.transpose(x_test)
        
    x_train_scaler = StandardScaler().fit(x_train)
    x_train = x_train_scaler.transform(x_train)
    x_test = x_train_scaler.transform(x_test)

    krr.fit(x_train,y_train)
    y_predict_test = krr.predict(x_test)
    y_predict_train = krr.predict(x_train)
    mse_test = mean_squared_error(y_test,y_predict_test)
    Rsquared_test = krr.score(x_test,y_test)
    mse_train = mean_squared_error(y_train,y_predict_train)
    Rsquared_train = krr.score(x_train,y_train)
    
    return y_predict_train,y_predict_test, mse_test, Rsquared_test, mse_train, Rsquared_train


def plot_predict(predict_test,y_test,predict_train,y_train,title):
    plt.scatter(y_train,predict_train,marker = 'v',alpha=0.2,label = 'train data')
    plt.scatter(y_test,predict_test,marker = 'o',alpha=0.5,label = 'test data')
    x = np.arange(min(y_train),max(y_train),0.01)
    xlow = np.arange(min(y_train)/0.9,max(y_train),0.01)
    xhigh = np.arange(min(y_train),max(y_train)/1.1,0.01)
    plt.plot(x,x,color='black',label='y = x')
    plt.plot(xlow,0.9*xlow,linestyle='--',color='red',alpha=0.5,label = 'y = 90% x')
    plt.plot(xhigh,1.1*xhigh,linestyle='--',color='red',alpha=0.5,label = 'y = 110% x')
    
    plt.xlabel('True Value')
    plt.ylabel('Predictive Value')
    plt.title(title)
    plt.legend()
    return


def print_mse(mse_test, Rsquared_test, mse_train, Rsquared_train):
    print('mse of test data: '+str(mse_test))
    print('mse of train data: '+str(mse_train))
    print('R-squared of test data: '+str(Rsquared_test))
    print('R-squared of train data: '+str(Rsquared_train))
    return


def predict_Band(feature_list,traindata,testdata,which):
    assert which in ['VB_ind','VB_dir','CB_dir','CB_ind','heat_of_formation'],"Unknown Prediction, please choose one in 'VB_ind','VB_dir','CB_dir','CB_ind','heat_of_formation'"
    krr = KernelRidge(alpha=1., kernel='polynomial',degree = 4)
    predict_train, predict_test, mse_test, Rsquared_test, mse_train, Rsquared_train= krr_predict(feature_list,krr,traindata,testdata,which)
    print_mse(mse_test, Rsquared_test, mse_train, Rsquared_train)
    return predict_train,predict_test
