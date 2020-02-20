import numpy as np 
import random as r
import math as m

temperature = 10000

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
    P = L.copy()
    a = r.randint(0,len(L)-1)
    b = r.randint(0,len(L)-1)
    while(b == a or a == cA and b == cB):
        b = r.randint(0,len(L)-1)
    temp = P[a]
    P[a] = P[b]
    P[b] = temp
    return P