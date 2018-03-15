
# coding: utf-8

# In[3]:


import pandas as pd
import open_database
import screen_3criteria as sc
perovskite,values,data_total=open_database.read_database() #3 dataframe
screening_data=sc.screening(data_total)                    #23 data after screening

data_total['water_splitting']=None
for i in screening_data.index:
    data_total['water_splitting'].iloc[i-1]=1

def input_screening(A_ion,B_ion,anion,mass,volume): 
    your_data=pd.DataFrame(columns=['anion', 'anion_X', 'anion_IE', 'A_ion', 'A_X', 'A_IE', 'A_s_R','A_p_R', 'A_d_R', 'A_aff', 
                                    'B_ion', 'B_X', 'B_IE','B_s_R','B_p_R','B_d_R', 'B_aff','volume','mass','density', 'A_R', 'B_R','X_A+B','X_A-B',
                                    'IE_A+B','IE_A-B','aff_A+B','aff_A-B','A_R_max','B_R_max','standard_energy'])
    for m in range(len(data_total)):
            if anion==data_total.iloc[m,:]['anion']:
                your_data=your_data.append(data_total.iloc[m,0:3])
                break
            else:
                continue
    for n in range(len(data_total)):
        if A_ion==data_total.iloc[n,3]:
            your_data = your_data.assign(A_ion=data_total.iloc[n,3],A_X=data_total.iloc[n,4], A_IE=data_total.iloc[n,5],
                                        A_s_R=data_total.iloc[n,6],A_p_R=data_total.iloc[n,7],A_d_R=data_total.iloc[n,8],
                                        A_aff=data_total.iloc[n,9])
            break
        else:
            continue
    for o in range(len(data_total)):
        if B_ion==data_total.iloc[o,:]['B_ion']:
            your_data = your_data.assign(B_ion=data_total.iloc[n,10],B_X=data_total.iloc[n,11], B_IE=data_total.iloc[n,12],
                                        B_s_R=data_total.iloc[n,13],B_p_R=data_total.iloc[n,14],B_d_R=data_total.iloc[n,15],
                                        B_aff=data_total.iloc[n,16],standard_energy=data_total.iloc[n,-1])
            break
        else:
            continue
    your_data['A_R']=your_data['A_s_R']+your_data['A_p_R']+your_data['A_d_R']
    your_data['B_R']=your_data['B_s_R']+your_data['B_p_R']+your_data['B_d_R']
    
    your_data['X_A+B']=your_data['A_X']+your_data['B_X']
    your_data['X_A-B']=your_data['A_X']-your_data['B_X']
    your_data['IE_A+B']=your_data['A_IE']+your_data['B_IE']
    your_data['IE_A-B']=your_data['A_IE']-your_data['B_IE']
    your_data['aff_A+B']=your_data['A_aff']+your_data['B_aff']
    your_data['aff_A-B']=your_data['A_aff']-your_data['B_aff']
    your_data['A_R_max']=your_data[['A_s_R', 'A_p_R', 'A_d_R']].max(axis=1)
    your_data['B_R_max']=your_data[['B_s_R', 'B_p_R', 'B_d_R']].max(axis=1)
    your_data['volume']=volume
    your_data['mass']=mass
    your_data['density']=mass/volume
    
    
    for i in range(len(data_total)):
        if A_ion==data_total.iloc[i,:]['A_ion']:
            if B_ion==data_total.iloc[i,:]['B_ion'] :
                if anion==data_total.iloc[i,:]['anion']:
                    if data_total.iloc[i,:]['water_splitting']==1:
                        comment='Yes,it can do water-slpitting'
                        return your_data,comment
                        break
                    else:
                        comment='No,it can\'t do water-splitting.'
                        return your_data,comment
                        break
                else:
                    continue
            else: 
                continue
        else:
            continue
        comment='The molecule is not in our database, so we need to predict'
        return your_data,comment
  