import numpy as np

#Books
#Copybooks = Books.sort().reverse()
books = []

def readFile():
    global maxi

    f= open("b_small.in","r")
    if f.mode == 'r':
        content = f.read()
        #print(contents.split("\n")[1].split(" "))
        maxi = int(content.split("\n")[0].split(" ")[0])
        contenList = content.split("\n")[1].split(" ")
        for c in contenList:
            books.append(int(c))
    
    f.close()

    if f.mode == 'r':
        return 1
    return 0