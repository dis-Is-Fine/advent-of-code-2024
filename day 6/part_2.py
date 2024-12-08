import os
import time
import datetime
import threading

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

def checkBounds(grid, position):
    if position[1] < 0:
        return False
    if position[0] < 0:
        return False
    if position[1] >= gridHeight:
        return False
    if position[0] >= gridWidth:
        return False
    return True

def printGrid(grid, guard, nextPosition):
    return
    for i in range(len(grid)):
        grid[i] = grid[i].copy()
    grid[guard[1]][guard[0]] = 'G'
    grid[nextPosition[1]][nextPosition[0]] = 'X'
    for line in grid:
        print(''.join(line))
    print('='*10)

def checkLoop(grid, guard, obstacle):
    for i in range(gridHeight):
        grid[i] = grid[i].copy()
    grid[obstacle[1]][obstacle[0]] = 'O'
    path = []

    for i in range(testPathLength):
        nextPosition = getNextPosition(guard)
        
        if not checkBounds(grid, nextPosition):
            return False
        
        for step in path:
            if step == guard:
                return obstacle
        
        while grid[nextPosition[1]][nextPosition[0]] == '#' or grid[nextPosition[1]][nextPosition[0]] == 'O':
            rotateGuard(guard)
            nextPosition = getNextPosition(guard)
        # printGrid(grid.copy(), guard, nextPosition)

        path.append(guard.copy())
        moveGuard(guard, nextPosition)
    
    return False

def solve(input):
    global gridHeight, gridWidth, testPathLength

    solution = 0
    
    grid = []
    guard = []
    guardStart = []
    path = []
    obstacles = []

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
    
    gridHeight= len(grid)
    gridWidth = len(grid[0])
    testPathLength = gridHeight*gridWidth

    guardInBounds = True

    while guardInBounds:

        nextPosition = getNextPosition(guard)
        
        if not checkBounds(grid, nextPosition):
            guardInBounds = False
            break

        while grid[nextPosition[1]][nextPosition[0]] == '#':
            rotateGuard(guard)
            nextPosition = getNextPosition(guard)

        if grid[nextPosition[1]][nextPosition[0]] == '^':
            nextPosition = getNextPosition(guard)
            moveGuard(guard, nextPosition)
            continue

        else:
            obstacle = checkLoop(grid.copy(),guardStart.copy(),nextPosition.copy())
            if obstacle == False:
                pass
            else:
                exists = False
                for o in obstacles:
                    if o == obstacle:
                        print(f'obstacle exists: {obstacle}')
                        exists = True
                        break
                
                if not exists:
                    solution += 1
                    obstacles.append(obstacle)
                    print(f'obstacle found {obstacle}')

        path.append(guard.copy())
        moveGuard(guard, nextPosition)
                
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

print("SOLUTION NOT YET WORKING CORRECTLY!!!")
# try:
#     input = open(__inputFile, 'r')
# except FileNotFoundError as e:
#     raise (e)

# __startTime = time.time()

# solution = solve(input)

# __runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%M:%S.%fs')
# print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')