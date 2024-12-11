import os
import time
import datetime

__test = True

__baseDir = os.path.dirname(__file__)

__testSet = [
    [os.path.join(__baseDir, "example_input.txt"), 2858]
]

__inputFile = os.path.join(__baseDir, 'input.txt')


def solve(input):
    solution = 0

    disk = []
    files = []
    x = 0

    for line in input:
        for i, char in enumerate(line.strip()):
            if i%2 == 0:
                files.append(len(disk))
                for a in range(int(char)):
                    disk.append(x)
                x += 1
            else:
                for a in range(int(char)):
                    disk.append(-1)

    for file in reversed(files):
        x = file
        while disk[x+1] == disk[file]:
            x += 1
            if x+1 >= len(disk):
                break
        fileSize = x - file + 1
        i = 0
        while i < len(disk) and i < file:
            foundEmpty = False
            while disk[i] == -1:
                e = i
                while disk[e+1] == -1:
                    e += 1
                emptySize = e - i + 1
                if emptySize >= fileSize:
                    foundEmpty = True
                    break
                else:
                    i += emptySize
            if foundEmpty:
                for x in range(fileSize):
                    disk[i+x] = disk[file+x]
                    disk[file+x] = -1
                break
            i += 1

    for i, part in enumerate(disk):
        if part != -1:
            solution += i*int(part)
            
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
    print(f'Tests completed succesfully in: {__runTime}\n{'='*45}')

try:
    input = open(__inputFile, 'r')
except FileNotFoundError as e:
    raise (e)

__startTime = time.time()

solution = solve(input)

__runTime = datetime.datetime.fromtimestamp(time.time()-__startTime).strftime('%M:%S.%fs')
print(f'Solution for the puzzle: {solution}\nElapsed time: {__runTime}')