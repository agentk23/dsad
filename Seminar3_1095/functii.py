import numpy as np
import pandas as pd


def nan_replace(x: np.ndarray):
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:, k[1]], axis=0)


def standardizare(x, std=True, ddof=0):
    x_ = x - np.mean(x, axis=0)
    if std:
        x_ = x_ / np.std(x, axis=0, ddof=ddof)
    return x_


def salvare(x, nume_linii=None, nume_coloane=None, nume_fisier="out.csv"):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    t.to_csv(nume_fisier)


def covariante_corelatii(x: np.ndarray, g):
    n, m = x.shape
    grupe = np.unique(g)
    q = len(grupe)
    covariante = np.empty(shape=(q, m, m))
    corelatii = np.empty(shape=(q, m, m))
    for k in range(q):
        y = x[g == grupe[k],:]
        if y.shape[0]>1:
            covariante[k] = np.cov(y,rowvar=False)
            corelatii[k] = np.corrcoef(y,rowvar=False)
    return covariante,corelatii,grupe

