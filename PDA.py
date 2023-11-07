import re
import numpy as np

currPos = 0

stateCount = 0
statesToIndex = {}
indexToStates = []

alphCount = 0
alphToIndex = {}
indexToAlph = []

symbCount = 0
symbToIndex = {}
indexToSymb = []

transCount = 0

accept = []

f = open("pda2.txt","r")
temp = f.read().splitlines()
f.close()

for line in temp:
    line = line.strip()
    if line == 'states:' or line == 'start:' or line == 'alphabet:' or line == 'transitions:' or line == 'accept:' or line == 'stack symbols:':
        if line == 'transitions:':
            trans = [[[[None,None] for j in range(alphCount)] for i in range(stateCount)] for k in range(symbCount)]
            print
        currPos += 1 
        continue
    if currPos == 1:
        statesToIndex[line] = stateCount
        indexToStates = indexToStates + [line]
        stateCount += 1
    if currPos == 2:
        start = line
    elif currPos == 3:
        alphToIndex[line] = alphCount
        indexToAlph = indexToAlph + [line]
        alphCount += 1
    elif currPos == 4:
        symbToIndex[line] = symbCount
        indexToSymb = indexToSymb + [line]
        symbCount +=1
    elif currPos == 5:
        temp = re.split(">|,",line)
        print(temp)
        trans[symbToIndex[temp[2]]][statesToIndex[temp[0]]][alphToIndex[temp[1]]] = [temp[3]]+[temp[4]]
    else:
        accept = accept + [line]

while(True):
    test = input("Enter a string:")

    currentState = start
    stack = 'Z'

    for i in range(len(test)):
        if test[0] not in indexToAlph:
            break

        print(currentState+','+test+','+stack+' ->',end=' ')
        action = trans[symbToIndex[stack[0]]][statesToIndex[currentState]][alphToIndex[test[0]]][1]
        currentState = trans[symbToIndex[stack[0]]][statesToIndex[currentState]][alphToIndex[test[0]]][0]

        if currentState == None:
            break

        if action == '$':
            stack = stack[1:]
        else:
            stack = action+stack[1:]

        test = test[1:]
    
    if test == '':
        test = 'ε'
    
    if test == 'ε' and stack == 'Z' and currentState in accept:
        print(currentState+','+test+','+stack+' -> ACCEPT')
    else:
        if currentState != None:
            print(currentState+','+test+','+stack+' -> REJECT')
        else:
            print('REJECT')