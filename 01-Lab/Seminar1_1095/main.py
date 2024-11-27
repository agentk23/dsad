from os import error

from functii import *
# i fucked up the whole code just bcs i wanted 
fisier = open("Sanatate.csv")

# linii = fisier.readlines()
# print(type(linii),linii,sep="\n")
def readDataFromCsv(file):

    data = []
    linii = file.readlines()
    n = len(linii)
    for i in range(n-1):
        linie = linii[i].split(",")
        try:
            entry = {
                'instanta': linie[0],
                'localitate': linie[1],
                'judet': linie[2],
                'nrMediciPrivati': linie[3],
                'nrMediciPublici': linie[4],
                'personalMediuPrivat': linie[5],
                'personalMediuPublic': linie[6],
                'medici': linie[7],

            }
            data.append(entry)
        except error:
            print(error)

    return data

data = readDataFromCsv(fisier)
print(data[1])


# linie0 = linii[0][:-1].split(",")
# nume_index = linie0[0]
# nume_variabile = linie0[1:]
# variabile_numerice = nume_variabile[2:]
# instante = []
#
# n = len(linii) - 1
# m = len(variabile_numerice)
#
# # print(variabile_numerice)
# tabel_linii = list()
# tabel_coloane = [[] for j in range(m)]
#
# for i in range(n):
#     linie = linii[i + 1][:-1].split(",")
#     # print(linie)
#     instante.append(linie[0])
#     tabel_linii.append([float(v) for v in linie[3:]])
#     for j in range(m):
#         tabel_coloane[j].append(float(linie[3+j]))

# def printTablePeLinii():
#     print("Tabelul memorat pe linii:")
#     for v in zip(instante, tabel_linii):
#         print(v)
#
#
# def printTabelPeColoane():
#     print("Tabelul memorat pe coloane:")
#     for v in zip(variabile_numerice, tabel_coloane):
#         print(v)

# cerinta1 = f1(instante,tabel_linii)
# print("\nCerinta 1")
# for v in cerinta1:
#     print(v,cerinta1[v],sep=":")
#
# cerinta2 = f2(variabile_numerice,tabel_coloane)
# print("\nCerinta 2")
# for v in cerinta2:
#     print(v,cerinta2[v],sep=":")

# cerinta 3: get data for input "judet"


def getDataForJudet(entries,judet):
    filteredData = []
    for i in range(len(entries)):
        if judet == entries[i].get('judet'):
            filteredData.append(entries[i])
    return filteredData
judet = "BV"
cerinta3 = getDataForJudet(data, judet)
def printCerinta3(cerinta3)
    for entry in cerinta3:
        print(entry)

