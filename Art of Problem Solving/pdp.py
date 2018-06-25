#!/usr/bin/python
#Roger D. Kerr
#Pyramid Descent Problem
import sys, os

def search(target):
    sequence = []
    searchHelper(target,0,0,sequence)
    return sequence

def searchHelper(curVal,row,pos,sequence):
    #base case
    if curVal == 1 and row == len(pyramid) - 1:
        return True
    elif row == len(pyramid) - 1:
        return False
    #check left
    if curVal % pyramid[row+1][pos] == 0:
        newTarget = curVal / pyramid[row+1][pos]
        sequence.append("L")
        if not searchHelper(newTarget,row+1,pos,sequence):
            sequence.pop()
        else:
            return True
    #check right
    if curVal % pyramid[row+1][pos+1] == 0:
        newTarget = curVal / pyramid[row+1][pos+1]
        sequence.append("R")
        if not searchHelper(newTarget,row+1,pos+1,sequence):
            sequence.pop()
        else:
            return True

def checkSequence(seq,target):
    total = pyramid[0][0]
    string = str(total)
    row = 1
    pos = 0
    for char in sequence:
        if char == 'L':
            num = pyramid[row][pos]
            string +=  ' * ' + str(num )
            total *= num
        else:
            pos += 1
            num = pyramid[row][pos]
            string += ' * ' + str(num)
            total *= num
        row += 1
    print(string,' = ',total)
    if total == target:
        print("Correct sequence")
    else:
        print("Incorrect sequence")

# Accept input file or use default if none given
if(len(sys.argv) < 2):
    inFile = 'pyramid_sample_input.txt'
else:
    inFile = sys.argv[1]
with open(inFile, 'r') as my_file:
    target = int(my_file.readline().split()[1])
    pyramid = []
    for line in my_file.read().splitlines():
        pyramid.append(list(map(int,line.split(','))))

curVal = target / pyramid[0][0]
sequence = search(curVal)

if 'input' in inFile:
    outFile = inFile.replace("input","output")
else:
    outFile = (os.path.splitext(inFile)[0]) + "_output.txt"
    
curVal = target / pyramid[0][0]
sequence = search(curVal)
#checkSequence(sequence,target)

with open(outFile, 'w') as my_file:
    my_file.write(''.join(sequence) + '\n')
    
