import re
import os

def refactorLeft(tape):
    tape = ['B']*10 + tape
    return tape

def refactorRight(tape):
    tape = tape + ['B']*10
    return tape

currPos = 0

stateCount = 0
statesToIndex = {}
indexToStates = []

alphCount = 0
alphToIndex = {}
indexToAlph = []

transCount = 0

accept = []

f = open("turing.txt","r")
temp = f.read().splitlines()
f.close()

for line in temp:
    line = line.strip()
    if line == 'states:' or line == 'start:' or line == 'alphabet:' or line == 'transitions:' or line == 'accept:':
        if line == 'transitions:':
            trans = [[[None,None,None] for j in range(alphCount)] for i in range(stateCount)]
        currPos += 1
        continue
    if currPos == 1:
        statesToIndex[line] = stateCount
        indexToStates = indexToStates + [line]
        stateCount += 1
    elif currPos == 2:
        start = line
    elif currPos == 3:
        accept = line
        statesToIndex[line] = stateCount
        indexToStates = indexToStates + [line]
        stateCount += 1
    elif currPos == 4:
        alphToIndex[line] = alphCount
        indexToAlph = indexToAlph + [line]
        alphCount += 1
    else:
        temp = re.split(">|,",line)
        trans[statesToIndex[temp[0]]][alphToIndex[temp[1]]] = [temp[2]]+[temp[3]]+[temp[4]]
        
# for element in indexToAlph:
#     print('\t\t\t'+element,end=' ')
# print()

# i = 0
# for row in trans:
#     print(indexToStates[i],end=' ')
#     for element in row:
#         print('\t '+str(element),end=' ')
#     i+=1
#     print() 

while(True):
    test = input("Enter a string:")
    currentState = start
    ptr = 0
    tape = [letter for letter in test]
    while(True):
        dummy = input()
        os.system('cls')
        if currentState == None:
            print("REJECT")
            break
        if currentState == accept:
            print("ACCEPT")
            break
        print(tape)
        print(currentState)
        print(ptr)
        next = trans[statesToIndex[currentState]][alphToIndex[tape[ptr]]]
        tape[ptr] = next[1]
        currentState = next[0]
        if next[2] == 'R':
            ptr += 1
            if (ptr>=len(tape)):
                tape = refactorRight(tape)
        elif next[2] == 'L':
            ptr -=1
            if (ptr<0):
                tape = refactorLeft(tape)
        else:
            ptr += 0