import lib as l

def score(system):
    daysMax = system.max 
    L = system.libraries
    daysPassed = 0
    cScore = 0
    cList = 0
    cursors = []
    for _ in range(len(L)):
        cursors.append(0)
    while(daysPassed < daysMax):
        for i in range(cList) :
            for _ in range(L[i].scannable_books_per_day) :
                if(cursors[i] < len(L[i].books)):
                    cScore += L[i].books[cursors[i]].score #get score of parsed book in lib
                    cursors[i] += 1 #increment parsing

        daysPassed += 1 #new day
        if(cList<=len(L)-1 and daysPassed >= L[cList].time) :
            cList += 1 #allow next lib to score when finally registered
    return cScore