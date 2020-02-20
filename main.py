# -*- coding: utf-8 -*-
import numpy as np
import lib as l
import simulation as s

def readFile(system):

    f= open("a_example.txt","r")
    #f= open("b_read_on.txt","r")
    if f.mode == 'r':
        content = f.read()
        libs = []

        print("Score")
        #List of scores of books
        scores = []
        a = int(content.split("\n")[0].split(" ")[0])
        la = content.split("\n")[1].split(" ")
        for i in range(a):
            scores.append(int(la[i]))

        print("Libraries")

        #Creating libs
        #print(int(content.split("\n")[0].split(" ")[1]))
        a = int(content.split("\n")[0].split(" ")[1])
        la = content.split("\n")
        for i in range(a):
            if (i%(a/10)==0):
                print(i,"lib over",a)
            #Creating the library from the file
            la2 = la[i*2+2].split(" ")
            newLib = l.Library(i,int(la2[1]), int(la2[2]))
            
            #books = []
            #Creating books
            b = int(content.split("\n")[i*2+2].split(" ")[0])
            lb = content.split("\n")[i*2+3].split(" ")
            for j in range(b):
                newBook = l.Book(int(lb[j]))
                newBook.score = scores[newBook.id]
                newLib.add_book(newBook)
            
            #Adding lib to the list
            libs.append(newLib)

        system.libraries = libs
        system.max = int(content.split("\n")[0].split(" ")[2])

        f.close()
        #print(system)
        return system
    
    f.close()
    return None

# def writeFile(system):
#     f= open("result.txt","w")
#     f.write("%d\n",system.nbrLibs)
#     for i in range(system.nbrLibs):
#         f.write("%d %d\n",system.libraries[i].id,system.libraries[i].nbrBooks)
#         for j in range(system.libraries[i].nbrBooks):
#             f.write("%d ",system.libraries[i].books[i])
#         f.write("\n")
#     f.close()

# ---------------------------------------------------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Liste des bibliothèques
    system = l.System()

    print("Reading ...")
    system = readFile(system)
    print("Done")
    
    # Lecture des entrées
    if (system != None):
        #print(system.libraries)
        print("Starting the simulation")
        score = s.score(system)
        print(score)