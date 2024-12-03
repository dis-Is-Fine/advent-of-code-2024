import os

test = False

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)

inputFile = os.path.join(baseDir, "example_input.txt" if test else "input.txt")
input = open(inputFile, "r")

leftArray = []
rightArray = []

for line in input:
    leftNumber, rightNumber = line.split("   ")
    leftArray.append(int(leftNumber))
    rightArray.append(int(rightNumber))

leftArray.sort()
rightArray.sort()

if len(leftArray) != len(rightArray):
    raise Exception("Left and right lists not of the same length!")

solution = 0

for i in range(len(leftArray)):
    solution += abs(leftArray[i] - rightArray[i])

print(f'Solution for the puzzle: {solution}')
