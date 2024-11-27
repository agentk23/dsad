from functii import *

fisier = open("Sanatate.csv")

linii = fisier.readlines()
# print(type(linii),linii,sep="\n")

linie0 = linii[0][:-1].split(",")
nume_index = linie0[0]
nume_variabile = linie0[1:]
variabile_numerice = nume_variabile[2:]
instante = []

n = len(linii) - 1
m = len(variabile_numerice)

# print(variabile_numerice)
tabel_linii = list()
tabel_coloane = [[] for j in range(m)]

for i in range(n):
    linie = linii[i + 1][:-1].split(",")
    # print(linie)
    instante.append(linie[0])
    tabel_linii.append([float(v) for v in linie[3:]])
    for j in range(m):
        tabel_coloane[j].append(float(linie[3+j]))

print("Tabelul memorat pe linii:")
for v in zip(instante, tabel_linii):
    print(v)

print("Tabelul memorat pe coloane:")
for v in zip(variabile_numerice, tabel_coloane):
    print(v)

cerinta1 = f1(instante,tabel_linii)
print("\nCerinta 1")
for v in cerinta1:
    print(v,cerinta1[v],sep=":")

cerinta2 = f2(variabile_numerice,tabel_coloane)
print("\nCerinta 2")
for v in cerinta2:
    print(v,cerinta2[v],sep=":")
