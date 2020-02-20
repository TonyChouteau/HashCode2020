#===================================
# Variables

maxi = 0
array = []

res = []
summ = 0

#===================================
# Functions

def readFile():
    global maxi

    f= open("b_small.in","r")
    if f.mode == 'r':
        content = f.read()
        #print(content.split("\n")[1].split(" "))
        maxi = int(content.split("\n")[0].split(" ")[0])
        contenList = content.split("\n")[1].split(" ")
        for c in contenList:
            array.append(int(c))
    
    f.close()

    if f.mode == 'r':
        return 1
    return 0

##

def choose():
    global maxi
    global summ
    global res

    currentSum = 0
    currentRes = []

    print(len(array), maxi)
    i = len(array)-1
    while (i>=0 and summ != maxi):
        if array[i]<(maxi-currentSum):
            currentRes.append(i)
            currentSum+=array[i]
            if (currentSum > summ):
                summ = currentSum
                res = list(currentRes)
        i-=1
        print(summ, res)
        

#===================================
# Entry Point

def main():    
    if (readFile()):
        choose()
 
if __name__ == '__main__':
    main()