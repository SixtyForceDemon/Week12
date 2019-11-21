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
    
def ScoreFinder(players, scores, name):
    if name in players:
        x = players.find(name)
        print('OUTPUT', name, 'got a score of', scores[x])
    else:
        PrintOutput('player not found')
        
def Union(list1, list2):
    list3 = list1 + list2
    list3 = list(dict.fromkeys(list3))
    return list3

def Intersection(list1, list2):
    list3 = []
    if len(list1) > len(list2):
        for element in list1:
            if element in list2:
                list3.append(element)
    else:
        for element in list2:
            if element in list1:
                list3.append(element)
    return list3
    

