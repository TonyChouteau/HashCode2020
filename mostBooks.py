import lib as l 
L = []

def getLib(libs,days):
    global L
    libsWorth = []
    for i in range(len(libs)):
        libsWorth.append((i,maxBooks(libs[i],days)))
    libsWorth.sort(key=takeSecond)
    libsWorth.reverse()
    j = 0
    while(libsWorth[j] in L):
        j+=1
    daysPassed = libs[libsWorth[j][0]].time
    if(days-daysPassed > 0):
        L.append(libsWorth[j])
        libs.pop(libsWorth[j][0])
        getLib(libs,days-daysPassed)

def maxBooks(lib,days):
    a = (days-lib.time)*lib.scannable_books_per_day
    if a>len(lib.books):
        return len(lib.books)
    else:
        return a

def takeSecond(e):
    return e[1]

def getLibList():
    global L
    return L