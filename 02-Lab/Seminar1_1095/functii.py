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
        cv = std / media
        t[variabile[j]] = (media, std, cv)
    return t


# Filtrare
def f3(x, judet):
    return x[2] == judet


# Sortare
def f4(x, k):
    return sum([x[2][i] for i in k])


def f5(x, k):
    valori = [x[1]]
    for i in k:
        valori.append(x[2][i])
    return (x[0], valori)


def f6(nume_coloane, t: dict, nume_index="", nume_fisier="out.csv"):
    fisier = open(nume_fisier, "wt")
    fisier.write(nume_index + "," + ",".join(nume_coloane) + "\n")
    for ch, v in t.items():
        fisier.write(ch + "," + ",".join([str(valoare) for valoare in v]) + "\n")
    fisier.close()
