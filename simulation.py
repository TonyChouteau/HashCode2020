import lib as l

def score(L,daysMax):
    daysPassed = 0
    cScore = 0
    cList = 0
    cursors = []
    for _ in range(len(L)):
        cursors.append(0)
    while(daysPassed < daysMax):
        for i in range(cList) :
            for _ in range(L[i].scannable_books_per_day) :
                cScore += L[i].books[cursors[i]] #get score of parsed book in lib
                cursors[i] += 1 #increment parsing

        daysPassed += 1 #new day
        if(daysPassed >= L[cList].time) :
            cList += 1 #allow next lib to score when finally registered
    return cScore