import os

test = False

baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)

inputFile = os.path.join(baseDir, "example_input.txt" if test else "input.txt")
input = open(inputFile, "r")

solution = 0

def checkNumbers(numbers):
    direction = 0
    
    for i in range(len(numbers)):
        if i == len(numbers)-1:
            return True

        diff = numbers[i+1] - numbers[i]

        if diff == 0 or abs(diff) > 3:
            break

        if direction == 0:
            direction = diff

        if direction < 0:
            if diff > 0:
                break
            
        if direction > 0:
            if diff < 0:
                break

    return False

solution = 0

for line in input:
    numbers = line.split()

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    safe = checkNumbers(numbers)
    if safe:
        solution += 1
    else:
        for i in range(len(numbers)):
            numbersCopy = numbers.copy()
            numbersCopy.pop(i)
            if checkNumbers(numbersCopy):
                solution += 1
                break

print(f'Solution for the puzzle: {solution}')
