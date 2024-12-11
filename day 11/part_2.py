import os
import time
import datetime
import functools

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 65601038650482]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

@functools.cache
def calculateStone(iteration, stone):
    if iteration >= 75:
        return 1
    stone = int(stone)
    if stone == 0:
        return calculateStone(iteration+1, 1)
    s = str(stone)
    l = len(s)
    x = int(l/2)
    if l%2 == 0:
        a, b = s[:x], s[x:]
        return calculateStone(iteration+1, int(a)) + \
                calculateStone(iteration+1, int(b))
    else:
        return calculateStone(iteration+1, stone*2024)
    

def solve(input):
    stones = input.readline().strip().split()
    
    solution = 0

    for stone in stones:
        solution += calculateStone(0, int(stone))
    
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

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%M:%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')