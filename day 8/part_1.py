import os
import time
import datetime
import itertools

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 14]
]

__inputFile = os.path.join(__baseDir, 'input.txt')

def checkBounds(position):
    if position[1] < 0:
        return False
    if position[0] < 0:
        return False
    if position[1] >= gridHeight:
        return False
    if position[0] >= gridWidth:
        return False
    return True

def solve(input):
    global gridHeight, gridWidth
    antennas = []
    antinodes = []

    for y, line in enumerate(input):
        for x, char in enumerate(line.strip()):
            if char != '.':
                frequencyExists = False
                for frequency in antennas:
                    if char == frequency[0]:
                        frequency[1].append([x, y])
                        frequencyExists = True
                        break
                if not frequencyExists:
                    antennas.append([char, [[x, y]]])
    
    gridHeight, gridWidth = y+1, x+1
    
    for frequency in antennas:
        for p in itertools.permutations(frequency[1]):
            distanceX = p[1][0] - p[0][0]
            distanceY = p[1][1] - p[0][1]
            antinode = [p[1][0]+distanceX, p[1][1]+distanceY]
            if checkBounds(antinode):
                if not any(a == antinode for a in antinodes):
                    antinodes.append(antinode)
    
    print(len(antinodes))
    return len(antinodes)


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

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')