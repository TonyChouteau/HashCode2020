import numpy as np
import lib as l

libs = []

def readFile():

    f= open("a_example.txt","r")
    if f.mode == 'r':
        content = f.read()

        #List of scores of books
        scores = []
        for i in range(int(contents.split("\n")[0].split(" ")[0])):
            scores.append(int(contents.split("\n")[0].split(" ")[i]))

        #Creating libs
        for i in range(int(contents.split("\n")[0].split(" ")[1])):
            #Creating the library from the file
            newLib = l.Library(i,int(contents.split("\n")[i*2+2].split(" ")[1], int(contents.split("\n")[i*2+2].split(" ")[2]))
            
            books = []
            #Creating books
            for j in range(int(contents.split("\n")[i*2+2].split(" ")[0])):
                books.append(l.Book(int(contents.split("\n")[i*2+3].split(" ")[j]), )

            #Creating libs to the list
            libs.append()

        maxi = int(content.split("\n")[0].split(" ")[0])
        contenList = content.split("\n")[1].split(" ")
        for c in contenList:
            books.append(int(c))
    
    f.close()

    if f.mode == 'r':
        return 1
    return 0

# ---------------------------------------------------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Programme principal ici

    print( "Test" )