# Prediction of perovskites' water-splitting ability

Our study aims at predicting whether a given perovskite has water-splitting ability. Since materials’ water-splitting ability is mainly determined by its band 
structure and heat of formation, our main task is to predict perovskite’s conduction/valence band energy and heat of formation based on atom’s easy accessible 
parameters like electronegativity, ionization energy, etc. Two methods are applied for predictions (i) kernel ridge regression (ii) neural network. We compare the 
predictions made by the two models and analyze the outliers. At last, a Graphical User Interface is setup which can read in a perovskite user input and return: (i) 
predicted values of the perovskite (ii) perovskite’s water splitting ability. 


GUI user guide:

1. Git clone or download our repo.
2. Double click file GUI.pyw (please wait for a while because it is a little slow...)
3. Input A_ion, B_ion, anion, mass and volume, then click ok. 
4. Please wait for a while, the text box on bottom will show the result on whether it can do water-splitting.

Jupyter notebook:
the jupyter notebook files under PredictWaterSplit show step by step how we develop our KRR and NN model. 

Requirements:

Before using our package, you should install these modules:
numpy
pandas
matplotlib
keras
tkinter
sklearn
sqlalchemy
itertools
scipy
