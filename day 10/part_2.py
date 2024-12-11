import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 81]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

directions = [[0,-1],[1,0],[0,1],[-1,0]]

def find(grid, pos, toFind):
    ret = []
    for dir in directions:
        try:
            if grid[pos[1]+dir[1]][pos[0]+dir[0]] == toFind:
                ret.append([pos[0]+dir[0], pos[1]+dir[1]])
        except IndexError as e:
            pass
    return ret

def branch(grid, paths):
    newPaths = []
    for path in paths:
        lastIndex = len(path)-1 
        nextDirections = find(grid, path[lastIndex], str(int(grid[path[lastIndex][1]][path[lastIndex][0]])+1))
        if nextDirections != False:
            for d in nextDirections:
                newPath = path.copy()
                newPath.append(d)
                newPaths.append(newPath)
        else:
            path = -1

    return newPaths

def solve(input):
    solution = 0

    grid = []
    startPoints = []

    for y,line in enumerate(input):
        grid.append(list(line.strip()))
        grid[y].append('x')
        for x,c in enumerate(line):
            if c == '0':
                startPoints.append([x,y])
    grid.append('x'*len(grid[0]))
    
    for start in startPoints:
        paths = [[start.copy()]]
        for i in range(9):
            paths = branch(grid, paths)
        solution += len(paths)

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