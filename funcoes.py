import random

def normaliza(dic):
    dicnorm = {}
    for continente, dicpais in dic.items():
        for pais, dicinfos in dicpais.items():
            dicnorm[pais] = dicinfos
            dicnorm[pais]["continente"] = continente
    return dicnorm

def sorteia_pais(dic):
    pais = random.choice(list(dic))
    return pais