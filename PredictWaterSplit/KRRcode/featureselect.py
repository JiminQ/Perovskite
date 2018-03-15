
import pandas as pd
import itertools

def feature_select(perovskite,n):
    data_combine = perovskite.drop(columns = ['anion','A_ion','B_ion'])
    corr = data_combine.corr(method='pearson').abs()
    features = list(data_combine.columns)
    corrlist = []
    combine = []
    for r in itertools.combinations(features,n):
        sum_corr = 0.
        for i in itertools.combinations(r,2):
            sum_corr = sum_corr + corr[i[0]][i[1]]
        corrlist.append(sum_corr)
        combine.append([r])
    sum_corr_list = pd.DataFrame({'sum of correlation':corrlist,'combination':combine})
    least_corr_list = sum_corr_list.sort_values(by = 'sum of correlation').head()
    return least_corr_list