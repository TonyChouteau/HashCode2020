import lib as l

def score(system):

    result = [

    daysMax = system.max 
    L = list(system.libraries)

    daysPassed = 0
    cScore = 0
    cList = 0

    daysBefore = 0

    cursors = []
    readBooks = []
    
    for _ in range(len(L)):
        cursors.append(0)

    while(daysPassed < daysMax):
        if (daysPassed%(daysMax/10) == 0):
                print(daysPassed,"days over",daysMax)
        for i in range(cList) :
            #print(i/cList*100,"%")
            for _ in range(L[i].scannable_books_per_day):
                id = -1
                bookSent = None
                while(len(L[i].books) > 0 and (id == -1 or id in readBooks)):
                    #print(len(L[i].books))
                    bookSent = L[i].books.pop(0)
                    id = bookSent.id
                #print(readBooks)
                #print(bookSent)
                if (bookSent is not None and id not in readBooks):
                    readBooks.append(id)
                    cScore += bookSent.score
                    system.libraries[i].scanned_books.append(id)

                bookSent = None

        daysPassed += 1 #new day
        if(cList<=len(L)-1 and daysPassed >= L[cList].time+daysBefore) :
            daysBefore+=L[cList].time
            cList += 1 #allow next lib to score when finally registered
    
    system.signed_libraries = cList
    #print()
    
    return system
