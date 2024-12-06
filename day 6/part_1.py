import os
import time
import datetime
import re

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 41]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

directions = [[0,-1],[1,0],[0,1],[-1,0]]
directionChars = [[0,'^'], [1,'>'], [2,'v'], [3,'<']]

def getNextPosition(guard):
    return [guard[0]+directions[guard[2]][0],
            guard[1]+directions[guard[2]][1]]

def rotateGuard(guard):
    direction = guard[2]
    guard[2] = direction + 1 if direction < 3 else 0
    return guard

def moveGuard(guard, nextPosition):
    guard[0] = nextPosition[0]
    guard[1] = nextPosition[1]

def checkBounds(grid, position):
    if position[1] < 0:
        return False
    if position[0] < 0:
        return False
    if position[1] >= len(grid):
        return False
    if position[0] >= len(grid[position[1]]):
        return False
    return True

def solve(input):
    solution = 0
    
    grid = []
    guard = []

    for y, line in enumerate(input):
        grid.append(list(line.strip()))
        if len(guard) == 0:
            for i, char in directionChars:
                x: int
                try:
                    x = line.index(char)
                except ValueError as e:
                    continue
                guard = [x, y, i]
                grid[y][x] = 'X'
                solution += 1
    
    guardInBounds = True

    while guardInBounds:
        nextPosition = getNextPosition(guard)
        
        if grid[guard[1]][guard[0]] == '.':
            grid[guard[1]][guard[0]] = 'X'
            solution += 1
        
        if not checkBounds(grid, nextPosition):
            return solution

        if grid[nextPosition[1]][nextPosition[0]] == '#':
            rotateGuard(guard)
            nextPosition = getNextPosition(guard)

        moveGuard(guard, nextPosition)



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