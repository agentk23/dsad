import numpy as np
import pandas as pd

from functii import nan_replace, standardizare, salvare, covariante_corelatii

pd.set_option("display.max_columns",None)
np.set_printoptions(5,threshold=10000,suppress=True)

set_date = pd.read_csv("Sanatate.csv",index_col=0)
# print(set_date,type(set_date),sep="\n")

exista_nan = set_date.isna().any().any()

variabile = list(set_date.columns)
# print(variabile)
variabile_numerice =variabile[2:]

x = set_date[variabile_numerice].values
# print(x,type(x),sep="\n")
nan_replace(x)
# print(x)

# Centrare date
x_c = standardizare(x,False)
salvare(x_c,set_date.index,variabile_numerice,"x_c.csv")
# Standardizare
x_std = standardizare(x)
salvare(x_std,set_date.index,variabile_numerice,"x_std.csv")

# Covariante/corelatii
v = np.cov(x,rowvar=False)
r = np.corrcoef(x,rowvar=False)
salvare(v,variabile_numerice,variabile_numerice,"V.csv")
salvare(r,variabile_numerice,variabile_numerice,"R.csv")

covariante,corelatii,grupe = covariante_corelatii(x,set_date["Judet"].values)
for k in range(len(grupe)):
    salvare(covariante[k],variabile_numerice,variabile_numerice,
            "v_"+grupe[k]+".csv")
    salvare(corelatii[k],variabile_numerice,variabile_numerice,
            "r_"+grupe[k]+".csv")
