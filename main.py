# -*- coding: utf-8 -*-
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
        for i in range(int(content.split("\n")[0].split(" ")[0])):
            scores.append(int(content.split("\n")[1].split(" ")[i]))

        #Creating libs
        print(int(content.split("\n")[0].split(" ")[1]))
        for i in range(int(content.split("\n")[0].split(" ")[1])):
            #Creating the library from the file
            newLib = l.Library(i,int(content.split("\n")[i*2+2].split(" ")[1]), int(content.split("\n")[i*2+2].split(" ")[2]))
            
            #books = []
            #Creating books
            for j in range(int(content.split("\n")[i*2+2].split(" ")[0])):
                newBook = l.Book(int(content.split("\n")[i*2+3].split(" ")[j]))
                newBook.score = scores[newBook.id]
                newLib.addBook(newBook)
            
            #Adding lib to the list
            libs.append(newLib)

        system.libraries = libs
        system.max = int(content.split("\n")[0].split(" ")[2])

        f.close()
        print(system)
        return system
    
    f.close()
    return None

# ---------------------------------------------------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Liste des bibliothèques
    system = l.System()

    system = readFile(system)
    
    # Lecture des entrées
    if (system != None):
        print(system.libraries)
        s.score(system)