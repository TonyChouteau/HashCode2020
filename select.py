import numpy as np 
import random as r
import math as m
import simulation as s

temperature = 10000
currentA = 0
currentB = 0
currentSys = []

def isSelected(score1, score2):
    global temperature
    temperature -= 1
    diff = score2-score1
    if diff > 0 : #La solution est meilleure, on la garde
        return True 
    else : #La solution est moins bonne
        r.seed()
        de = r.random() - (1-m.exp(-diff/temperature))
        if de > 0 : #Avec une proba de plus en plus faible, on la garde
            return True
        else : #Avec une proba de plus en plus forte, on la rejette
            return False

def permute(cSys,cA,cB):
    global temperature
    nSys = cSys.copy()
    libnS = cSys.libraries
    a = r.randint(0,len(libnS)-1)
    b = r.randint(0,len(libnS)-1)
    while(b == a or a == cA and b == cB):
        b = r.randint(0,len(libnS)-1)
    temp = libnS[a]
    libnS[a] = libnS[b]
    libnS[b] = temp
    cA,cB = a,b
    temperature -= 1
    return nSys

def nextStep():
    global temperature, currentA, currentB, currentSys
    assert temperature > 0
    temperature -= 1
    s1 = s.score(currentSys)
    newSys = permute(currentSys,currentA,currentB)
    s2 = s.score(newSys)
    if isSelected(s1,s2):
        currentSys = s2

def takeSecond(e):
    return e[1]

def sortSys(sys):
    libRatio = []
    for i in range(len(sys.libraries)):
        regTime = sys.libraries[i].time
        scannable = sys.libraries[i].scannable_books_per_day
        weight = 0
        for j in range(scannable):
            weight += sys.libraries[i].books[j].score
        libRatio.append((i,(weight*scannable)/regTime))
    libRatio.sort(key=takeSecond)
    res = []
    for k in range(len(libRatio)):
        res.append(sys.libraries[libRatio[k][0]])
    return res
