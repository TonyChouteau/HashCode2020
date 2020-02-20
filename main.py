import numpy as np
import lib as l

libs = []

def readFile():

    f= open("a_example.txt","r")
    if f.mode == 'r':
        content = f.read()
        #print(contents.split("\n")[1].split(" "))
        books.append(l.Library)

        maxi = int(content.split("\n")[0].split(" ")[0])
        contenList = content.split("\n")[1].split(" ")
        for c in contenList:
            books.append(int(c))
    
    f.close()

    if f.mode == 'r':
        return 1
    return 0