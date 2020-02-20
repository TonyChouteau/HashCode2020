import numpy as np
import lib as l
import simulation as s

def readFile(system):

    f= open("a_example.txt","r")
    if f.mode == 'r':
        content = f.read()
        libs = []

        #List of scores of books
        scores = []
        for i in range(int(contents.split("\n")[0].split(" ")[0])):
            scores.append(int(contents.split("\n")[1].split(" ")[i]))

        #Creating libs
        for i in range(int(contents.split("\n")[0].split(" ")[1])):
            #Creating the library from the file
            newLib = l.Library(i,int(contents.split("\n")[i*2+2].split(" ")[1], int(contents.split("\n")[i*2+2].split(" ")[2])))
            
            books = []
            #Creating books
            for j in range(int(contents.split("\n")[i*2+2].split(" ")[0])):
                newBook = l.Book(int(contents.split("\n")[i*2+3].split(" ")[j]))
                newBook.score = score[newBook.ID_book]
                books.append(newBook)

            #Adding books to the lib
            lib.books = books
            
            #Adding lib to the list
            libs.append(lib)

        system.librarys = libs
        system.max = int(contents.split("\n")[0].split(" ")[2])

        f.close()
        return libs
    
    f.close()
    return None

# ---------------------------------------------------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Liste des bibliothèques
    system = l.System()

    # Lecture des entrées
    if (readFile(system) != None):
        print(system.libs, system.max)
        #s.score(system)
    
