import os
import time
import datetime

__test = False

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)

inputFile = os.path.join(baseDir, "example_input.txt" if __test else "input.txt")
input = open(inputFile, "r")

__startTime = time.time()

leftArray = []
rightArray = []

for line in input:
    leftNumber, rightNumber = line.split("   ")
    leftArray.append(int(leftNumber))
    rightArray.append(int(rightNumber))

leftArray.sort()
rightArray.sort()

solution = 0

for i in range(len(leftArray)):
    solution += abs(leftArray[i] - rightArray[i])

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')
