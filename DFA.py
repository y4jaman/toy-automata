import re

test = "0011111"

currPos = 0

stateCount = 0
statesToIndex = {}
indexToStates = []

alphCount = 0
alphToIndex = {}
indexToAlph = []

transCount = 0

accept = []

f = open("dfa.txt","r")
temp = f.read().splitlines()
f.close()

for line in temp:
    line = line.strip()
    if line == 'states:' or line == 'start:' or line == 'alphabet:' or line == 'transitions:' or line == 'accept:':
        if line == 'transitions:':
            trans = [[None for j in range(alphCount)] for i in range(stateCount)]
        currPos += 1 
        continue
    if currPos == 1:
        statesToIndex[line] = stateCount
        indexToStates = indexToStates + [line]
        stateCount += 1
    if currPos == 2:
        start = line
    if currPos == 3:
        alphToIndex[line] = alphCount
        indexToAlph = indexToAlph + [line]
        alphCount += 1
    if currPos == 4:
        temp = re.split(">|,",line)
        trans[statesToIndex[temp[0]]][alphToIndex[temp[1]]] = temp[2]
    if currPos == 5:
        accept = accept + [line]

for element in indexToAlph:
    print('\t'+element,end=' ')
print()

i = 0
for row in trans:
    print(indexToStates[i],end=' ')
    for element in row:
        print('\t'+str(element),end=' ')
    i+=1
    print() 

while(True):
    print()
    test = input("Enter a string:")
    flag = False
    currentState = start
    i = 0
    for i in range(len(test)):
        print(currentState+','+test[i:]+'->',end=' ')
        currentState = trans[statesToIndex[currentState]][alphToIndex[test[i]]]
        if currentState == None:
            print("REJECT")
            flag = True
            break

    if not flag:
        if currentState in accept:
            print("ACCEPT,ε")
        else:
            print("REJECT")