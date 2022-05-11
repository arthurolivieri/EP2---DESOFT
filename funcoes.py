import random
from math import *

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

def adiciona_em_ordem(nome,dist,lista):
    saida=lista
    if not lista:
        saida.append([nome,dist])
        return saida

    flag=True

    for i in lista:
        if dist<i[1]:
            flag=False
    
    if flag==False:
        for i in range (len(lista)):
            if dist<lista[i][1]:
                saida.insert(i,[nome,dist])
                break
    
    elif flag == True:
        saida.append([nome,dist])

    return saida


def esta_na_lista(nome,lista):
    flag=False
    for i in range (len(lista)):
        if nome == lista[i][0]:
            flag=True
    return flag

def sorteia_letra(palavra,restrito):
    l=list(palavra.lower())
    if ' ' in l:
        try:
            while True:
                l.remove(' ')
        except ValueError:
            pass
    if '-' in l:
        try:
            while True:
                l.remove('-')
        except ValueError:
            pass
    if ',' in l:
        l.remove(',')
    print(restrito)
    for i in range (len(restrito)):
        if restrito[i] in l:
            try:
                while True:
                    l.remove(restrito[i])
            except ValueError:
                pass
    if not l:
        return ""
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    else:
        caracter=random.choice(res)
        return caracter

def haversine(r,p1,l1,p2,l2):
    p=(radians(p2)-radians(p1))/2
    l=(radians(l2)-radians(l1))/2
    c1=sin(p)**2+(cos(radians(p1))*cos(radians(p2))*sin(l)**2)
    c2=c1**(1/2)
    d=2*r*asin(c2)
    return d