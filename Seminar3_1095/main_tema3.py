import pandas as pd

from functii import nan_replace_t

t_religii = pd.read_csv("tema3_in/Religious.csv",index_col=0)
exista_nan = t_religii.isna().any().any()
if exista_nan:
    nan_replace_t(t_religii)
