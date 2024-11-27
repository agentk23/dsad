from functii import *

fisier = open("Sanatate.csv")

linii = fisier.readlines()
# print(type(linii),linii,sep="\n")

linie0 = linii[0][:-1].split(",")
nume_index = linie0[0]
nume_variabile = linie0[1:]
variabile_numerice = nume_variabile[2:]
instante = []
judete = []
localitati = []

n = len(linii) - 1
m = len(variabile_numerice)

# print(variabile_numerice)
tabel_linii = list()
tabel_coloane = [[] for j in range(m)]

for i in range(n):
    linie = linii[i + 1][:-1].split(",")
    judete.append(linie[2])
    localitati.append(linie[1])
    # print(linie)
    instante.append(linie[0])
    tabel_linii.append([float(v) for v in linie[3:]])
    for j in range(m):
        tabel_coloane[j].append(float(linie[3 + j]))

# print("Tabelul memorat pe linii:")
# for v in zip(instante, tabel_linii):
#     print(v)

# print("Tabelul memorat pe coloane:")
# for v in zip(variabile_numerice, tabel_coloane):
#     print(v)

cerinta1 = f1(instante, tabel_linii)
# print("\nCerinta 1")
# for v in cerinta1:
#     print(v,cerinta1[v],sep=":")

cerinta2 = f2(variabile_numerice, tabel_coloane)
# print("\nCerinta 2")
# for v in cerinta2:
#     print(v,cerinta2[v],sep=":")

print("\nCerinta 3")
judet_filtru = "CV"
# cerinta3_ = filter(lambda x:f3(x,judet_filtru),zip(instante,judete,tabel_linii))
cerinta3_ = filter(lambda x: f3(x, judet_filtru), zip(instante, localitati, judete, tabel_linii))
cerinta3 = dict()
for v in cerinta3_:
    cerinta3[v[0] + "_" + v[1]] = v[3]
    # print(v)
# for ch,v in cerinta3.items():
#     print(ch,v,sep=":")

print("\nCerinta 4")
variabile_sortare = ["NrMedici_Privat", "PersonalMediu_privat"]

cerinta4_ = sorted(zip(instante, localitati, tabel_linii),
                   key=lambda x: f4(x, [variabile_numerice.index(v) for v in variabile_sortare]),
                   reverse=True)
cerinta4 = dict()
for v in cerinta4_:
    cerinta4[v[0] + "_" + v[1]] = v[2]
for ch, v in cerinta4.items():
    print(ch, v, sep=":")

print("\nCerinta 5")
variabile_selectate = ["PersonalMediu_public", "PersonalMediu_privat"]
cerinta5 = dict(map(lambda x: f5(x, [variabile_numerice.index(v) for v in variabile_selectate]),
                    zip(instante, localitati, tabel_linii)))
for ch, v in cerinta5.items():
    print(ch, v, sep=":")
coloane = ["Localitate"]
for v in variabile_selectate:
    coloane.append(v)
f6(coloane, cerinta5, nume_index, "cerinta5.csv")
