import sys

import numpy as np
import pandas as pd

from functii import nan_replace_t, acp, tabel_varianta
from grafice import plot_varianta

np.set_printoptions(precision=5,
                    threshold=sys.maxsize,
                    suppress=True)
set_date = pd.read_csv("data_in/Y_DNA_Tari.csv",index_col=0)
variabile_observate = list(set_date)[1:]
exista_nan = set_date.isna().any().any()
if exista_nan:
    nan_replace_t(set_date)

x = set_date[variabile_observate].values
alpha,a,c,r = acp(x)
# print(alpha)

# Analiza variantei componentelor
t_varianta = tabel_varianta(alpha)
t_varianta.to_csv("acp_out/varianta.csv")
plot_varianta(alpha)
