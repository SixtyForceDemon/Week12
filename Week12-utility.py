#Elliot Kwilinski
#CS 102 Section E
#Week 12

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    with open(filename, 'r') as f:
        listOfData = f.readlines
    return listOfData
    
def UpdateString(string1, string2, index):
    newString = string1.replace(string1[index], string2)
    print(newString)
    
def FinalWordCount(givenList, givenString):
    return givenList.count(givenString)
    

