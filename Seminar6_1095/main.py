import numpy as np
import pandas as pd


def f_cerinta4(t: pd.DataFrame):
    # print(t)
    x = t.values
    p = (x.T / np.sum(x, axis=1)).T
    k = np.argmax(p, axis=0)
    return pd.Series(t.index[k], t.columns)


def f_cerinta5(t: pd.DataFrame):
    # print(t)
    x = t.values[:,:-1]
    # print(x)
    y = t.values[:,-1]
    # print(y)
    v = np.average(x, weights=y, axis=0)
    return pd.Series(v, t.columns[:-1])


educatie = pd.read_csv("data_in/Educatie.csv", index_col=0)

educatie_p = educatie.apply(func=lambda x: x / x.sum(), axis=1)
# print(educatie_p)
cerinta1 = educatie_p.sort_values(by="PersoaneAnalfabete", ascending=False)[["PersoaneAnalfabete"]]
cerinta1.to_csv("data_out/Cerinta1.csv")

populatie = pd.read_csv("data_in/PopulatieJudete.csv", index_col=0)
educatie_pop = educatie.merge(populatie, left_index=True, right_index=True)
# print(educatie_pop)
cerinta2 = educatie_pop.apply(
    lambda x: (x["PersoaneAnalfabete"] + x["FaraScoala"]) * 100000 / x["Populatie"], \
    axis=1)
cerinta2.name = "Analfabeti_FaraScoala"
# print(cerinta2)
assert isinstance(cerinta2, pd.Series)
cerinta2.sort_values(ascending=False, inplace=True)
cerinta2.to_csv("data_out/Cerinta2.csv")

ro_nuts = pd.read_csv("data_in/RO_NUTS.csv", index_col=0)
educatie_ = educatie.merge(ro_nuts["Regiune"], left_index=True, right_index=True)
cerinta3 = educatie_.groupby(by="Regiune").sum()
cerinta3.to_csv("data_out/Cerinta3.csv")

cerinta4 = educatie_.groupby(by="Regiune").apply(func=f_cerinta4, include_groups=False)
cerinta4.to_csv("data_out/Cerinta4.csv")

cerinta5 = educatie_pop.merge(ro_nuts["Regiune"], left_index=True, right_index=True) \
    .groupby(by="Regiune").apply(func=f_cerinta5, include_groups=False)
cerinta5.to_csv("data_out/Cerinta5.csv")
