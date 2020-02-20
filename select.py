import numpy as np 
import random as r
import math as m

temperature = 10000

def isSelected(score1, score2):
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
