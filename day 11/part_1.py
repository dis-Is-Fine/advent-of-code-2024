import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 55312]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

def solve(input):
    stones = input.readline().strip().split()
    
    for i in range(25):
        newStones = []
        for stone in stones:
            s = str(stone)
            l = len(s)
            x = int(l/2)
            stone = int(stone)
            if stone == 0:
                newStones.append(1)
            elif l%2 == 0:
                a, b = s[:x], s[x:]
                newStones.append(int(a))
                newStones.append(int(b))
            else:
                newStones.append(stone*2024)
        stones = newStones
            
    return len(stones)


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