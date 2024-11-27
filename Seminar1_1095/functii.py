import math


def f1(instante, tabel):
    t = dict()
    for i in range(len(instante)):
        t[instante[i]] = sum(tabel[i])
    return t


def f2(variabile, tabel):
    t = dict()
    for j in range(len(variabile)):
        x = tabel[j]
        media = sum(x) / len(x)
        std = math.sqrt(sum([(v - media) * (v - media) for v in x]) / len(x))
        cv = std/media
        t[variabile[j]] = (media,std,cv)
    return t

