import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def collectoutlier(pred_compare):
    outlier_CB_ind = pd.concat([pred_compare[(pred_compare.CB_ind_pred<(0.9*pred_compare.CB_ind))],pred_compare[(pred_compare.CB_ind_pred>(1.1*pred_compare.CB_ind))]])
    outlier_VB_ind = pd.concat([pred_compare[(pred_compare.VB_ind_pred<(0.9*pred_compare.VB_ind))],pred_compare[(pred_compare.VB_ind_pred>(1.1*pred_compare.VB_ind))]])
    outlier_CB_dir = pd.concat([pred_compare[(pred_compare.CB_dir_pred<(0.9*pred_compare.CB_dir))],pred_compare[(pred_compare.CB_dir_pred>(1.1*pred_compare.CB_dir))]])
    outlier_VB_dir = pd.concat([pred_compare[(pred_compare.VB_dir_pred<(0.9*pred_compare.VB_dir))],pred_compare[(pred_compare.VB_dir_pred>(1.1*pred_compare.VB_dir))]])
    outliers = [outlier_CB_ind.index,
            outlier_VB_ind.index,
            outlier_CB_dir.index,
            outlier_VB_dir.index]
    result = set(outliers[0])
    for s in outliers[1:]:
        result.intersection_update(s)
    recur_outliers = pred_compare.loc[list(result)]
    return recur_outliers


def plot_outlier(predict_test,y_test,predict_outlier,y_outlier,title):
    #plt.figure(figsize=(6.5,4))
    plt.scatter(y_test,predict_test,marker = 'o',alpha=0.2,label = 'test data')
    plt.scatter(y_outlier,predict_outlier,marker = 'o',alpha=0.4,label = 'recurring outlier')
    x = np.arange(min(y_test),max(y_test),0.01)
    xlow = np.arange(min(y_test)/0.9,max(y_test),0.01)
    xhigh = np.arange(min(y_test),max(y_test)/1.1,0.01)
    plt.plot(x,x,color='black',label='y = x')
    plt.plot(xlow,0.9*xlow,linestyle='--',color='red',alpha=0.5,label = 'y = 90% x')
    plt.plot(xhigh,1.1*xhigh,linestyle='--',color='red',alpha=0.5,label = 'y = 110% x')
    plt.xlabel('True Value')
    plt.ylabel('Predicted Value')
    plt.title(title)
    plt.legend()
#plt.savefig(title+'.png', dpi = 350)
    return