
# coding: utf-8

# In[ ]:


def model():
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.wrappers.scikit_learn import KerasRegressor
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import KFold
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    model = Sequential()
    model.add(Dense(19, input_dim=19, kernel_initializer='normal', activation='relu'))
    model.add(Dense(12, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


# In[ ]:


def prediction_hof(data_total,new_data):
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.wrappers.scikit_learn import KerasRegressor
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import KFold
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    seed = 21899
    df5=new_data.loc[0:1]
    X = data_total[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
                    'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
                    'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    Y = data_total[['heat_of_formation']].values
    X1 = df5[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R','A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R','B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    X_train_pn,X_test_pn,y_train,y_test1 = train_test_split(X, Y, test_size=0.20,random_state=seed)
    X_train_scaler = StandardScaler().fit(X_train_pn)
    X_train = X_train_scaler.transform(X_train_pn)
    np.random.seed(seed)
    estimator = KerasRegressor(build_fn= model,
        epochs=500, batch_size=10000, verbose=0)
    history = estimator.fit(X_train, y_train, validation_split=0.33, epochs=500, 
        batch_size=5000, verbose=0)
    X2 = X_train_scaler.transform(X1)
    predictions_h_o_f = estimator.model.predict(X2,batch_size=30000)
    return predictions_h_o_f


# In[ ]:


def prediction_on_dir_VB(data_total,new_data):
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.wrappers.scikit_learn import KerasRegressor
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import KFold
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    seed = 21899
    df5=new_data.loc[0:1]
    X = data_total[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    Y = data_total[['VB_dir']].values
    X1 = df5[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    X_train_pn,X_test_pn,y_train,y_test1 = train_test_split(X, Y, test_size=0.20,random_state=seed)
    X_train_scaler = StandardScaler().fit(X_train_pn)
    X_train = X_train_scaler.transform(X_train_pn)
    np.random.seed(seed)
    estimator = KerasRegressor(build_fn= model,
        epochs=500, batch_size=10000, verbose=0)
    history = estimator.fit(X_train, y_train, validation_split=0.33, epochs=500, 
        batch_size=5000, verbose=0)
    X2 = X_train_scaler.transform(X1)
    predictions_dir_VB = estimator.model.predict(X2,batch_size=30000)
    return predictions_dir_VB


# In[ ]:


def prediction_on_dir_CB(data_total,new_data):
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.wrappers.scikit_learn import KerasRegressor
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import KFold
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    seed = 21899
    df5=new_data.loc[0:1]
    X = data_total[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    Y = data_total[['CB_dir']].values
    X1 = df5[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    X_train_pn,X_test_pn,y_train,y_test1 = train_test_split(X, Y, test_size=0.20,random_state=seed)
    X_train_scaler = StandardScaler().fit(X_train_pn)
    X_train = X_train_scaler.transform(X_train_pn)
    np.random.seed(seed)
    estimator = KerasRegressor(build_fn= model,
        epochs=500, batch_size=10000, verbose=0)
    history = estimator.fit(X_train, y_train, validation_split=0.33, epochs=500, 
        batch_size=5000, verbose=0)
    X2 = X_train_scaler.transform(X1)
    predictions_dir_CB = estimator.model.predict(X2,batch_size=30000)
    return predictions_dir_CB


# In[ ]:


def prediction_on_indir_VB(data_total,new_data):
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.wrappers.scikit_learn import KerasRegressor
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import KFold
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    seed = 21899
    df5=new_data.loc[0:1]
    X = data_total[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    Y = data_total[['VB_ind']].values
    X1 = df5[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    X_train_pn,X_test_pn,y_train,y_test1 = train_test_split(X, Y, test_size=0.20,random_state=seed)
    X_train_scaler = StandardScaler().fit(X_train_pn)
    X_train = X_train_scaler.transform(X_train_pn)
    np.random.seed(seed)
    estimator = KerasRegressor(build_fn= model,
        epochs=500, batch_size=10000, verbose=0)
    history = estimator.fit(X_train, y_train, validation_split=0.33, epochs=500, 
        batch_size=5000, verbose=0)
    X2 = X_train_scaler.transform(X1)
    predictions_indir_VB = estimator.model.predict(X2,batch_size=30000)
    return predictions_indir_VB


# In[ ]:


def prediction_on_indir_CB(data_total,new_data):
    from keras.models import Sequential
    from keras.layers import Dense
    from keras.wrappers.scikit_learn import KerasRegressor
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import KFold
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    seed = 21899
    df5=new_data.loc[0:1]
    X = data_total[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    Y = data_total[['CB_ind']].values
    X1 = df5[['anion_X', 'anion_IE', 'A_X', 'A_IE', 'A_s_R',
       'A_p_R', 'A_d_R', 'A_aff' , 'B_X', 'B_IE', 'B_s_R', 'B_p_R',
       'B_d_R', 'B_aff', 'volume', 'mass', 'density', 'A_R', 'B_R']].values
    X_train_pn,X_test_pn,y_train,y_test1 = train_test_split(X, Y, test_size=0.20,random_state=seed)
    X_train_scaler = StandardScaler().fit(X_train_pn)
    X_train = X_train_scaler.transform(X_train_pn)
    np.random.seed(seed)
    estimator = KerasRegressor(build_fn= model,
        epochs=500, batch_size=10000, verbose=0)
    history = estimator.fit(X_train, y_train, validation_split=0.33, epochs=500, 
        batch_size=5000, verbose=0)
    X2 = X_train_scaler.transform(X1)
    predictions_indir_CB = estimator.model.predict(X2,batch_size=30000)
    return predictions_indir_CB

