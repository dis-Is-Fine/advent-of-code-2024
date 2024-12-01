import os

test = False

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)

inputFile = os.path.join(baseDir, "example_input.txt" if test else "input.txt")
input = open(inputFile, "r")

leftArray = []
rightArray = []

for line in input:
    leftNumber, rightNumber = line.split("   ")
    leftArray.append(int(leftNumber));
    rightArray.append(int(rightNumber));

leftArray.sort()
rightArray.sort()

if len(leftArray) != len(rightArray):
    raise Exception("Left and right lists not of the same length!")

arrayLength = len(leftArray)
solution = 0

for i in range(arrayLength):
    currentNumber = leftArray[i]
    try:
        multiplier = 0
        index = rightArray.index(currentNumber)
        while rightArray[index] == currentNumber:
            # check if we won't exceed array bounds
            if index + 1 < arrayLength:
                index += 1
                multiplier += 1
            else:
                break
        solution += multiplier*currentNumber 
    # remember: currentNumber may not be present in RightArray
    except (ValueError) as e:
        continue

print(f'Solution for the puzzle: {solution}')
