import numpy as np 
import random as r
import math as m
import simulation as s

temperature = 10000
currentA = 0
currentB = 0
currentList = []

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

def permute(L,cA,cB):
    global temperature
    P = L.copy()
    a = r.randint(0,len(L)-1)
    b = r.randint(0,len(L)-1)
    while(b == a or a == cA and b == cB):
        b = r.randint(0,len(L)-1)
    temp = P[a]
    P[a] = P[b]
    P[b] = temp
    cA,cB = a,b
    temperature -= 1
    return P

def nextStep(L):
    global temperature, currentA, currentB, currentList
    assert temperature > 0
    temperature -= 1
    sL = s.score(currentList)
    P = permute(L,currentA,currentB)
    sP = s.score(P)
    if isSelected(sL,sP):
        currentList = sP