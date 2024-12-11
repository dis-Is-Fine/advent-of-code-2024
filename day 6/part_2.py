import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 6]
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

def checkBounds(position):
    if position[1] < 0:
        return False
    if position[0] < 0:
        return False
    if position[1] >= lenY:
        return False
    if position[0] >= lenX:
        return False
    return True

def simulateGuard(grid, guard, testPathLength):
    path = []

    for i in range(testPathLength):
        nextPosition = getNextPosition(guard)
        
        if not checkBounds(nextPosition):
            return False
        
        while grid[nextPosition[1]][nextPosition[0]] == '#':
            rotateGuard(guard)
            nextPosition = getNextPosition(guard)
        
        if not checkBounds(nextPosition):
            return False
        
        if any(step == guard for step in path):
            return True
        
        path.append(guard.copy())
        moveGuard(guard, nextPosition)
    
    return False

def printGrid(grid, obstructions):
    for i in range(len(grid)):
        grid[i] = grid[i].copy()
    for o in obstructions:
        grid[o[1]][o[0]] = 'O'
    for line in grid:
        print(''.join(line))
    print('='*10)

def solve(input):
    solution = 0
    
    grid = []
    guard = []
    guardStart = []
    possibleObstructions = []

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
                guardStart = [x, y, i]
                grid[y][x] = 'X'
    
    guardInBounds = True

    global lenY, lenX
    lenY = len(grid)
    lenX = len(grid[0])

    while guardInBounds:
        nextPosition = getNextPosition(guard)

        if not checkBounds(nextPosition):
            break

        while grid[nextPosition[1]][nextPosition[0]] == '#':
            rotateGuard(guard)
            nextPosition = getNextPosition(guard)
            
        if not checkBounds(nextPosition):
            break
        
        moveGuard(guard, nextPosition)

        if grid[guard[1]][guard[0]] != 'X':
            possibleObstructions.append([guard[0],guard[1]])

    temp = []
    for o in possibleObstructions:
        if not any(t == o for t in temp):
            temp.append(o)
    possibleObstructions = temp

    for i, o in enumerate(possibleObstructions):
        grid[o[1]][o[0]] = '#'
        if simulateGuard(grid, guardStart.copy(), 15000):
            solution += 1
            print(f'found {o}')
        grid[o[1]][o[0]] = '.'
        print(f'checked {i} of {len(possibleObstructions)}')

    print(solution)
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
    print(f'Tests completed succesfully in: {__runTime}\n{"="*45}')


try:
    input = open(__inputFile, 'r')
except FileNotFoundError as e:
    raise (e)

__startTime = time.time()

solution = solve(input)

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%H:%M:%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')