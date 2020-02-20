import numpy as np

#Books
#Copybooks = Books.sort().reverse()
books = []
booksNbr = 0
libNbr = 0
totalTime = 0

def readFile():
    global maxi

    f= open("a_example.txt","r")
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

# ---------------------------------------------------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Liste des bibliothèques
    libraries = []

    # Lecture des entrées
    readFile()
