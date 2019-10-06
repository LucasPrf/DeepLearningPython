import pandas as pd
from sklearn.model_selection import train_test_split

previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv');

prev_trein,prev_teste,class_prev,class_teste=train_test_split(previsores,classe,test_size=0.25)
