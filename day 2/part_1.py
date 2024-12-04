import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, 'example_input.txt'), 2]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

def solve(input):
    solution = 0

    for line in input:
        numbers = line.split()
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        
        direction = 0

        for i in range(len(numbers)):
            if i == len(numbers)-1:
                solution += 1
                break

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
        
    return solution

def test(testSet):
    for i, [testInputFile, solution] in enumerate(testSet, 1):
        try:
            testInput = open(testInputFile, 'r')
        except FileNotFoundError as e:
            raise(e)
        
        if solve(testInput) != solution:
            raise RuntimeError(f'Test {i} failed!')

        else:
            yield f'Test {i} passed'

if __test:
    __startTime = time.time()

    for msg in test(__testSet):
        print(msg)

    __runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
    print(f'Tests completed succesfully in: {__runTime}\n{'='*45}')


try:
    input = open(__inputFile, 'r')
except FileNotFoundError as e:
    raise (e)

__startTime = time.time()

solution = solve(input)

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')
