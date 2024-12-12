import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input_1.txt"), 140],
    [os.path.join(__baseDir, "example_input_2.txt"), 772],
    [os.path.join(__baseDir, "example_input_3.txt"), 1930]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

directions = [[0,-1],[1,0],[0,1],[-1,0]]

def printGrid(grid, groupSet=None):
    return
    for y in range(len(grid)):
        grid[y] = grid[y].copy()

    if groupSet != None:
        for group in groupSet:
            for plant in group[0]:
                grid[plant[1]][plant[0]] = group[1]+grid[plant[1]][plant[0]]+"\033[0m"

    for line in grid:
        t = ''
        for c in line:
            t = t + c
        print(t)
    
    print('\n'*2)

def checkInBounds(pos):
    if pos[0] < 0 or pos[0] >= gridWidth:
        return False
    if pos[1] < 0 or pos[1] >= gridHeight:
        return False
    return True

def groupPlants(grid, initPos):
    group = [initPos]
    lastAdded = [initPos]
    foundNewPlants = True

    while foundNewPlants:
        lastAddedCopy = lastAdded.copy()
        for i in range(len(lastAddedCopy)):
            lastAddedCopy[i] = lastAddedCopy[i].copy()
        lastAdded = []

        for pos in lastAddedCopy:
            plant = grid[pos[1]][pos[0]]
            for dir in directions:
                npos = [pos[0]+(dir[0]*2), pos[1]+(dir[1]*2)]
                if not checkInBounds(npos):
                    continue
                checkedPlant = grid[npos[1]][npos[0]]
                if plant == checkedPlant:
                    if not any(p == npos for p in group):
                        lastAdded.append(npos)
                        group.append(npos)

        # printGrid(grid.copy(), [[lastAdded, "\033[0;31m"],[group, "\033[0;32m"]])
        if len(lastAdded) == 0:
            foundNewPlants = False    
    return group

def getPerimeter(grid, group):
    perimeter = 0
    for plant in group:
        for dir in directions:
            checkPos = [plant[0]+dir[0], plant[1]+dir[1]]
            checkVal = grid[checkPos[1]][checkPos[0]]
            if checkVal != ' ':
                perimeter += 1
    
    return perimeter

def solve(input):
    solution = 0

    grid = []
    groups = []

    for y, line in enumerate(input):
        line = line.strip()
        grid.append([' ']*(len(line)*2+1))
        t = []
        for x, char in enumerate(line):
            t.append(' ')
            t.append(char)
        t[0] = '|'
        t.append('|')
        grid.append(t)
    
    global gridHeight, gridWidth
    gridHeight = len(grid)
    gridWidth = len(grid[0])

    grid[0] = ['-']*gridWidth
    grid.append(['-']*(gridWidth))

    for y in range(gridHeight):
        if y%2 == 0:
            continue

        for x in range(gridWidth):
            if x%2 == 0:
                continue

            if x+2 < gridWidth:
                if grid[y][x] != grid[y][x+2]:
                    grid[y][x+1] = '|'

            if y+2 < gridHeight:
                if grid[y][x] != grid[y+2][x]:
                    grid[y+1][x] = '-'
            # printGrid(grid.copy())

    for y in range(gridHeight):
        if y%2 == 0:
            continue
        for x in range(gridWidth):
            if x%2 == 0:
                continue
            checkedBefore = False
            for group in groups:
                if any(p == [x,y] for p in group):
                    checkedBefore = True
                    break
            if checkedBefore:
                continue
            groups.append(groupPlants(grid, [x, y]))
        # print(f'{y} of {gridHeight}')

    for group in groups:
        # print(group)
        area = len(group)
        # print(area)
        perimeter = getPerimeter(grid, group)
        # print(perimeter)
        # printGrid(grid.copy(), [[group, "\033[0;33m"]])
        solution += area*perimeter

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