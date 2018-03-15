
# coding: utf-8

# In[ ]:


import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import numpy as np

def read_database():
    engine = create_engine('sqlite:///cubic_perovskites.db')
    with engine.connect() as conn, conn.begin():
        keyvalues = pd.read_sql_table('number_key_values', conn)
        textvalues = pd.read_sql_table('text_key_values', conn)
        keys = pd.read_sql_table('keys', conn)
        systems = pd.read_sql_table('systems',conn)
    
    CB_ind = keyvalues[(keyvalues.key=='CB_ind')]
    gllbsc_ind_gap = keyvalues[(keyvalues.key=='gllbsc_ind_gap')]
    CB_dir = keyvalues[(keyvalues.key=='CB_dir')]
    VB_dir = keyvalues[(keyvalues.key=='VB_dir')]
    VB_ind = keyvalues[(keyvalues.key=='VB_ind')]
    gllbsc_dir_gap = keyvalues[(keyvalues.key=='gllbsc_dir_gap')]
    heat_of_formation = keyvalues[(keyvalues.key=='heat_of_formation_all')]
    standard_energy = keyvalues[(keyvalues.key=='standard_energy')]

    valuelist=[CB_dir,VB_dir,VB_ind,gllbsc_dir_gap,gllbsc_ind_gap,heat_of_formation,standard_energy]
    values = CB_ind
    for x in valuelist:
        values = pd.merge(values,x,how='outer',on='id')
    
    values.set_index('id',inplace=True)
    values.columns=['key','CB_ind','key','CB_dir','key','VB_dir','key','VB_ind','key','gllbsc_dir_gap','key','gllbsc_ind_gap','key','heat_of_formation','key','standard_energy']

    values=values.drop(columns='key')
    #values=values.drop(labels='key',axis=1)
    
    A_ion = textvalues[(textvalues.key=='A_ion')]
    B_ion = textvalues[(textvalues.key=='B_ion')]
    anion = textvalues[(textvalues.key=='anion')]
    electroneg = pd.read_csv('electronegativity.csv')
    electroneg.columns = ['value', 'electronegativity']
    A_electroneg=pd.merge(A_ion,electroneg,how='left',on='value')
    B_electroneg=pd.merge(B_ion,electroneg,how='left',on='value')
    ionization=pd.read_excel('ionization energy.xlsx')
    A_values=pd.merge(A_electroneg,ionization,how='left',on='value')
    B_values=pd.merge(B_electroneg,ionization,how='left',on='value')
    Rmax = pd.read_excel('Rmax.xlsx')
    A_values = pd.merge(A_values,Rmax,how='left',on='value')
    B_values = pd.merge(B_values,Rmax,how='left',on='value')
    affinity = pd.read_excel('electron affinities.xlsx')
    A_values = pd.merge(A_values,affinity,how='left',on='value')
    B_values = pd.merge(B_values,affinity,how='left',on='value')

    A_values.columns=['key','A_ion','id','A_X','A_IE','A_s_R','A_p_R','A_d_R','A_aff']
    B_values.columns=['key','B_ion','id','B_X','B_IE','B_s_R','B_p_R','B_d_R','B_aff']
    cation_values=pd.merge(A_values,B_values,how='outer',on='id')

    anion_electronegativity=[3.04,3.62,3.30666,3.15333,3.44,3.48666,3.17333]
    #this is calculated from the average of atom's electronegativity
    anion_ionization=[14.53414,14.88631,13.92342,12.53204,13.61806,15.19167,14.22878]
    #this is calculated from the average of atom's ionization
    anion_data = pd.DataFrame({'value':['N3','O2F','O2N','O2S','O3','OFN','ON2'],'electronegativity':anion_electronegativity,'first ionization energy':anion_ionization})

    anion_values=pd.merge(anion,anion_data,how='left',on='value')
    anion_values.columns=['key','anion','id','anion_X','anion_IE']
    perovskite_values=pd.merge(anion_values,cation_values,how='outer',on='id')

    volume = pd.DataFrame({'id': systems.id, 'volume':systems.volume})
    mass = pd.DataFrame({'id': systems.id, 'mass':systems.mass})
    perovskite=pd.merge(perovskite_values,volume,how='left',on='id')
    perovskite=pd.merge(perovskite,mass,how='left',on='id')
    perovskite=perovskite.drop(columns=['key','key_x','key_y'])
    perovskite.set_index('id',inplace=True)
    perovskite['density']=perovskite['mass']/perovskite['volume']
    # remove all the NaN 
    perovskite = perovskite.fillna(0.)
    perovskite['A_R']=perovskite['A_s_R']+perovskite['A_p_R']+perovskite['A_d_R']
    perovskite['B_R']=perovskite['B_s_R']+perovskite['B_p_R']+perovskite['B_d_R']
    
    perovskite['X_A+B']=perovskite['A_X']+perovskite['B_X']
    perovskite['X_A-B']=perovskite['A_X']-perovskite['B_X']
    perovskite['IE_A+B']=perovskite['A_IE']+perovskite['B_IE']
    perovskite['IE_A-B']=perovskite['A_IE']-perovskite['B_IE']
    perovskite['aff_A+B']=perovskite['A_aff']+perovskite['B_aff']
    perovskite['aff_A-B']=perovskite['A_aff']-perovskite['B_aff']
    perovskite['A_R_max']=perovskite[['A_s_R', 'A_p_R', 'A_d_R']].max(axis=1)
    perovskite['B_R_max']=perovskite[['B_s_R', 'B_p_R', 'B_d_R']].max(axis=1)
    
    # remove all the NaN line
    values = values[(values.CB_ind > 0.0)]
    
    data_total=pd.merge(perovskite,values,how='outer',left_index=True,right_index=True)
    return perovskite,values,data_total
    

