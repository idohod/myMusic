import secrets
import os
from Rhythm import *
from Transition import *

def printIndexes(size):
    for i in range(size):
        print(i, end=" ")
        print("\t",end=" ")
    print("\n")
    return

def printConting(size):
     counter = 1
     for i in range(size):
         if (i % 4 == 1):
             print("e", end="")
         elif(i % 4 == 2):
            print("n", end="")
         elif(i % 4 == 3):
            print("a", end="")
         else:           
            print(counter, end = "")
            counter = counter + 1
         print("\t",end = " ")        
     print("\n")
     return

def writeLine(file):
    for i in range(95):
        file.write("-")
    file.write("\n")
    return
  
def writeAllRhythm(file,rhythm):
    file.write("\n")
    file.write(rhythm.rhythmInfo())
    writeLine(file)
    return

def writeAllTransition(file,transition):
    file.write("\n")
    file.write(transition.TransitionInfo())
    writeLine(file)
    return

def strLen(string):
    counter = 0
    for i in string:
        counter = counter + 1
    return counter

def subString(chosenFile):
    if (chosenFile.find(".rtf",0,len) == -1):
         chosenFile = chosenFile + ".rtf"
    return chosenFile

def setPermission(chosenFile,files,permission):
    if(chosenFile in files):
        while(permission == ""):
            userChoise = input("start from beginning or continue from last point? (enter b\c) ")
            if(userChoise == "b"):
                permission = "w"
            elif(userChoise == "c"):
                permission = "a"
            else:
                permission = ""
    else:
        permission = "x"

    return permission


r1 = Rhythm()
r1.randAndSetRhythm()

nums = [1,2,3,4]
rhythmRepet = secrets.choice(nums)

printIndexes(r1.size)
print(r1.rhythmInfo())

path = 'C:/Users/ADMIN/Desktop/myMusic'
files = os.listdir(path)
print(files)
permission = ""
chosenFile = input("choose file from list or enter new name: ")
len = strLen(chosenFile)

chosenFile = subString(chosenFile)
permission = setPermission(chosenFile,files,permission)

file = open(path + "/" + chosenFile,permission)
for i in range(rhythmRepet):
    writeAllRhythm(file,r1)

index = input("choose index to start Transition: ")
ind = int(index)

printConting(r1.size)

t1 = Transition()
t1.randTransition(ind)
t1.setTransition(ind,r1)

writeAllTransition(file,t1)
file.close()

print(t1.TransitionInfo())