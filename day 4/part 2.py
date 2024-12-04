import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, 'example_input_2.txt'), 9],
]

__inputFile = os.path.join(__baseDir, 'input.txt')

directionsLUT = [ 
    [[1,1],     [[[0,2], [1,-1]],   [[2,0], [-1,1]]]],
    [[-1,-1],   [[[-2,0], [1,-1]],  [[0,-2], [-1,1]]]],
]
directionCount = len(directionsLUT)

def findMAS(grid, x, y, direction):
    if grid[y][x] != 'M':
        return False
    
    searchX = x + direction[0]
    searchY = y + direction[1]

    try:
        if(grid[searchY][searchX] != 'A'):
            return False
    except IndexError as e:
        return False

    searchX += direction[0]
    searchY += direction[1]

    try:
        if(grid[searchY][searchX] != 'S'):
            return False
    except IndexError as e:
        return False
    
    return True


def solve(input):
    solution = 0

    grid = []

    for line in input:
        grid.append(list(line))
    
    # Add a buffer to prevent negative searchY at first line from looking to the last line
    # check example_input_3.txt to see the edge case
    # No need to add buffer for searchX as it already has a buffer (new line character)
    grid.append(list('.')*len(grid[0]))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for direction in directionsLUT:
                if not findMAS(grid, x, y, direction[0]):
                    continue
                for direction in direction[1]:
                    if not findMAS(grid, x+direction[0][0], y+direction[0][1], direction[1]):
                        continue
                    solution += 1
                    break

    return solution


def test(testSet):
    for i, [testInputFile, solution] in enumerate(testSet, 1):
        try:
            testInput = open(testInputFile, 'r')
        except FileNotFoundError as e:
            raise(e)
        
        a=solve(testInput)
        if a != solution:
            print(f'Expected answer: {solution}\nRecieved answer: {a}')
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