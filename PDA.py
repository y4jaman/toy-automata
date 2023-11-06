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

stack = ['Z0']

accept = []

f = open("pda.txt","r")
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
        trans[statesToIndex[temp[0]]][alphToIndex[temp[1]]] = [temp[2]]+[temp[3]]+[temp[4]]
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
    stack = ['Z0']
    print()
    test = input("Enter a string:")
    flag = False
    currentState = start
    for i in range(len(test)):
        if test[0] not in alphToIndex:
            break
        print(currentState+','+test+',',end='')
        print(stack,end=' ')
        print('->',end=' ')
        if trans[statesToIndex[currentState]][alphToIndex[test[0]]][1] == 'pop': 
            currentState = trans[statesToIndex[currentState]][alphToIndex[test[0]]][0]#move to new state specified by the transition table
            if stack[len(stack)-1] == trans[statesToIndex[currentState]][alphToIndex[test[0]]][2]:
                stack = stack[:len(stack)-1] #pop from stack
            else:
                break
        else:
            stack = stack + [trans[statesToIndex[currentState]][alphToIndex[test[0]]][2]] #push to stack
            currentState = trans[statesToIndex[currentState]][alphToIndex[test[0]]][0] #move to state specifice by the transition table
        test = test[1:]
        if currentState == None:
            print("REJECT")
            flag = True
            break

    if test == '':
        test = 'ε'
    if not flag:
        if stack == ['Z0'] and test == 'ε' and currentState in accept:
            print(currentState+','+test+',',end='')
            print(stack,end=' ')
            print('-> ACCEPT')
        else:
            print(currentState+','+test+',',end='')
            print(stack,end=' ')
            print("-> REJECT")